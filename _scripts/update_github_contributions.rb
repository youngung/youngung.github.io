require "date"
require "json"
require "net/http"
require "time"

query = <<~GRAPHQL
  query($login: String!, $from: DateTime!, $to: DateTime!) {
    user(login: $login) {
      contributionsCollection(from: $from, to: $to) {
        contributionCalendar {
          weeks {
            contributionDays {
              date
              contributionCount
              contributionLevel
            }
          }
        }
      }
    }
  }
GRAPHQL

levels = %w[NONE FIRST_QUARTILE SECOND_QUARTILE THIRD_QUARTILE FOURTH_QUARTILE]
token = ENV["GITHUB_TOKEN"]
abort "Set GITHUB_TOKEN to refresh the GitHub contribution calendar." if token.to_s.empty?

endpoint = URI("https://api.github.com/graphql")
user = "youngung"
now = Time.now.utc
today = now.to_date
years = today.year.downto(today.year - 2).map do |year|
  first = Date.new(year, 1, 1)
  last = [Date.new(year, 12, 31), today].min
  through = [Time.utc(last.year, last.month, last.day, 23, 59, 59), now].min
  request = Net::HTTP::Post.new(endpoint)
  request["Authorization"] = "Bearer #{token}"
  request["Content-Type"] = "application/json"
  request.body = JSON.generate(query: query, variables: {
    login: user,
    from: Time.utc(year, 1, 1).iso8601,
    to: through.iso8601
  })

  response = Net::HTTP.start(endpoint.host, endpoint.port, use_ssl: true, open_timeout: 10, read_timeout: 15) do |http|
    http.request(request)
  end
  abort "GitHub GraphQL returned HTTP #{response.code} for #{year}." unless response.is_a?(Net::HTTPSuccess)

  result = JSON.parse(response.body)
  if result["errors"]
    abort "GitHub GraphQL rejected the contribution calendar query for #{year}: #{result['errors'].map { |error| error['message'] }.join('; ')}"
  end
  weeks = result.dig("data", "user", "contributionsCollection", "contributionCalendar", "weeks")
  abort "GitHub GraphQL returned no contribution calendar for #{year}." unless weeks

  calendar = weeks.flat_map { |week| week.fetch("contributionDays") }.to_h { |day| [day.fetch("date"), day] }

  days = Array.new(first.wday)
  months = []
  (first..last).each do |date|
    cell = calendar.fetch(date.iso8601)
    count = cell.fetch("contributionCount")
    level = levels.index(cell.fetch("contributionLevel"))
    raise "Unexpected GitHub contribution data for #{date}" unless level && count.is_a?(Integer) && count >= 0

    months << { month: date.strftime("%b"), column: days.length / 7 + 1 } if date.day == 1
    days << { date: date.iso8601, count: count, level: level }
  end
  {
    year: year,
    total: days.compact.sum { |day| day[:count] },
    months: months,
    days: days
  }
end

output = File.expand_path("../_data/github_contributions.json", __dir__)
File.write("#{output}.tmp", JSON.pretty_generate({ user: user, through: today.iso8601, years: years }) + "\n")
File.rename("#{output}.tmp", output)

require "jekyll-scholar"

# Keep publication status groups separate from chronological year groups.
# Prefer status = {accepted|submitted}; also accept the existing year/journal
# conventions without altering the original bibliography or inventing a year.
module PublicationGroups
  STATUSES = %w[accepted submitted].freeze

  def group_value(key, item)
    return super unless key == "publication_year"

    status = %w[status year journal].map { |field| item[field].to_s.strip.downcase }
      .find { |value| STATUSES.include?(value) }
    return status.capitalize if status

    year = item["year"].to_s.strip
    year.empty? ? "Undated" : year
  end

  def group_compare(key, first, second)
    return super unless key == "publication_year"

    publication_group_rank(first) <=> publication_group_rank(second)
  end

  def publication_group_rank(value)
    case value
    when "Submitted" then [3, 0, ""]
    when "Accepted" then [2, 0, ""]
    when /\A\d{4}\z/ then [1, value.to_i, ""]
    else [0, 0, value.to_s]
    end
  end
end

Jekyll::Scholar::BibliographyTag.prepend(PublicationGroups)

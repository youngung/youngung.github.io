require "jekyll-scholar"

# Keep publication status groups separate from chronological year groups.
# Prefer the status field; also accept the existing year/journal
# conventions without altering the original bibliography or inventing a year.
module PublicationGroups
  STATUS_LABELS = {
    "in preparation" => "In Preparation",
    "under preparation" => "In Preparation",
    "submitted" => "Submitted",
    "accepted" => "Accepted"
  }.freeze

  def group_value(key, item)
    return super unless key == "publication_year"

    status_label = %w[status year journal].filter_map do |field|
      STATUS_LABELS[item[field].to_s.downcase.split.join(" ")]
    end.first
    return status_label if status_label

    year = item["year"].to_s.strip
    year.empty? ? "Undated" : year
  end

  def group_compare(key, first, second)
    return super unless key == "publication_year"

    publication_group_rank(first) <=> publication_group_rank(second)
  end

  def render_groups(groups)
    excluded = Array(config["exclude_publication_groups"])
    return super unless group_keys.first == "publication_year" && !excluded.empty?

    super(groups.reject { |label, _entries| excluded.include?(label) })
  end

  def publication_group_rank(value)
    case value
    when "In Preparation" then [4, 0, ""]
    when "Submitted" then [3, 0, ""]
    when "Accepted" then [2, 0, ""]
    when /\A\d{4}\z/ then [1, value.to_i, ""]
    else [0, 0, value.to_s]
    end
  end
end

Jekyll::Scholar::BibliographyTag.prepend(PublicationGroups)

require "nokogiri"
require "uri"

# Kramdown appends footnotes after the source content. Keep lecture navigation
# below those notes, including in future lectures using the same link labels.
Jekyll::Hooks.register [:pages, :documents], :post_convert do |page|
  next unless page.relative_path.delete_prefix("/").start_with?("assets/lecture_notes/", "_lectures/")
  next unless page.output_ext == ".html"

  fragment = Nokogiri::HTML::DocumentFragment.parse(page.content)
  # Source-file links work in VS Code. Resolve their published URLs at build
  # time using Jekyll's page metadata, including any custom permalinks.
  fragment.css("a[href]").each do |link|
    source, anchor = link["href"].split("#", 2)
    next unless source.start_with?("/") && source.end_with?(".md")

    source = URI::DEFAULT_PARSER.unescape(source.delete_prefix("/"))
    target = (page.site.pages + page.site.documents).find do |candidate|
      candidate.relative_path.delete_prefix("/") == source
    end
    raise "Internal lecture target not found: #{source}" unless target

    link["href"] = "#{page.site.baseurl}#{target.url}#{anchor ? "##{anchor}" : ""}"
  end

  menu_link = if page.relative_path.delete_prefix("/").start_with?("assets/lecture_notes/")
                fragment.css("a").find { |a| a.text.strip == "강의 목록" }
              end
  menu = menu_link&.ancestors&.find { |node| %w[table p nav].include?(node.name) }
  if menu
    separator = menu.previous_element
    separator.remove if separator&.name == "hr"
    navigation = Nokogiri::XML::Node.new("nav", fragment.document)
    navigation["class"] = "lecture-navigation"
    navigation["aria-label"] = "강의 이동"
    navigation.add_child(menu.unlink)
    fragment.add_child(navigation)
  end

  fragment.css('.footnotes[role="doc-endnotes"]').each do |notes|
    notes.add_class("lecture-footnotes")
    heading = Nokogiri::XML::Node.new("p", fragment.document)
    heading["class"] = "lecture-footnotes-label"
    heading.content = "각주"
    notes.prepend_child(heading)
  end
  page.content = fragment.to_html
end

require "nokogiri"

# Kramdown appends footnotes after the source content. Keep lecture navigation
# below those notes, including in future lectures using the same link labels.
Jekyll::Hooks.register [:pages, :documents], :post_convert do |page|
  next unless page.path.start_with?("assets/lecture_notes/")
  next unless page.output_ext == ".html"

  fragment = Nokogiri::HTML::DocumentFragment.parse(page.content)
  menu_link = fragment.css("a").find { |a| a.text.strip == "강의 목록" }
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

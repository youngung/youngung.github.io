---
layout: about
title: about
permalink: /
subtitle: <a href='#'>Changwon National University</a>

profile:
  align: right
  image: # prof_pic.jpg
  image_circular: false # crops the image to make it circular
  more_info: # >
#    <p>555 your office number</p>
#    <p>123 your address street</p>
#    <p>Your City, State 12345</p>

selected_papers: true # includes a list of papers marked as "selected={true}"
social: true # includes social icons at the bottom of the page

announcements:
  enabled: true # includes a list of news items
  scrollable: true # adds a vertical scroll bar if there are more than 3 news items
  limit: 5 # leave blank to include all the news in the `_news` folder

latest_posts:
  enabled: true
  scrollable: true # adds a vertical scroll bar if there are more than 3 new posts items
  limit: 3 # leave blank to include all the blog posts
---

[재료금속공학과; Department of Materials Science and Metallurgy](https://www.changwon.ac.kr/msm/main.do)

Welcome to the Mechanics of Materials Laboratory

<link rel="stylesheet" href="{{ '/assets/css/github-contributions.css' | relative_url }}">

<div class="home-activity my-4">
<figure class="text-center mb-0">
  <img
    src="{{ '/assets/animations/crail_forming_springback.gif' | relative_url }}"
    alt="Finite element animation of C-rail forming and springback"
    width="720"
    height="852"
    style="width: 100%; max-width: 440px; height: auto;"
  />
  <figcaption class="mt-2">
Crystal plasticity finite element simulation of C-rail forming and springback using $\Delta$EVPSC model
  </figcaption>
</figure>
{% include github_contributions.liquid %}
</div>

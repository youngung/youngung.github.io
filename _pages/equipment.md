---
layout: page
title: equipment
permalink: /equipment/
description:
nav: true
nav_order: 3
horizontal: false
horizontal: false
---

{% assign sorted_items = site.equipment | sort:"importance" %}

{% for tool in sorted_items %}
  * {{ tool.title }}:
	 - 구매시기  : {{ tool.purchased_year }}
	 - 주요 spec : {{ tool.spec }}
	{% if tool.loc %}
	 - 설치 장소 : {{ tool.loc }}
	{% endif %}
	{% if tool.img %}
		<img class="card-img" src="{{ tool.img | relative_url }}" style="object-fit: cover; width: 30%" alt="image">
	{% endif %}
{% endfor %}

---
layout: page
title: lectures
permalink: /lectures/
description: 강의자료 collection
nav: true
nav_order: 3
horizontal: false
---

{% for lecture in site.lectures %}

  <h1>
	<a href="{{ lecture.url }}">
	  * {{ lecture.title }}
	</a>
	<h6>
		대상: {{lecture.target}}
	</h6>
	<h6>
		필요 선수과목: {{lecture.prerequisite}}
	</h6>
  </h1>
{% endfor %}

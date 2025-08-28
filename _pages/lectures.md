---
layout: page
title: lectures
permalink: /lectures/
description: 강의자료
nav: true
nav_order: 3
horizontal: false
---


{% for lecture in site.lectures %}
  <h2>
	<a href="{{ lecture.url }}">
	  * {{ lecture.title }}
	</a>
  </h2>
{% endfor %}

---
layout: page
title: lectures
permalink: /lectures/
description: 강의자료
nav: true
nav_order: 3
horizontal: false
---

<ul>
	{% for lecture in site.lectures %}

	<li>
	<h3> {{ lecture.title }} </h3>
	<p> {{ lecture.content | markdownify }} </p>
	</li>


	{% endfor %}
</ul>

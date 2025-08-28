---
layout: page
title: projects
permalink: /projects/
description:
nav: true
nav_order: 3
horizontal: false
horizontal: false
---

{% for project in site.projects %}
  * {{ project.title }}:   {{ project.begin }} ~ {{ project.end }}   **{{ project.funder }}**
{% endfor %}

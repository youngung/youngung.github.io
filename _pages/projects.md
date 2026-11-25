---
layout: page
title: projects
permalink: /projects/
description:
nav: true
nav_order: 3
---

{% assign projects = site.projects | sort: "begin" | reverse %}
{% assign today = site.time | date: "%Y-%m-%d" %}
{% assign upcoming = "" %}
{% assign ongoing = "" %}
{% assign completed = "" %}

{% for project in projects %}
{% assign start_date = project.begin | date: "%Y-%m-%d" %}
{% assign end_date = project.end | date: "%Y-%m-%d" %}
{% capture item %}

<li>{{ project.title | escape }}: {{ start_date }} ~ {{ end_date }} <strong>{{ project.funder | escape }}</strong></li>
  {% endcapture %}
  {% if start_date > today %}
    {% assign upcoming = upcoming | append: item %}
  {% elsif end_date != "" and end_date < today %}
    {% assign completed = completed | append: item %}
  {% else %}
    {% assign ongoing = ongoing | append: item %}
  {% endif %}
{% endfor %}

{% if upcoming != "" %}

## 시작 예정 과제

<ul>{{ upcoming }}</ul>
{% endif %}

{% if ongoing != "" %}

## 수행 중인 과제

<ul>{{ ongoing }}</ul>
{% endif %}

{% if completed != "" %}

## 완료된 과제

<ul>{{ completed }}</ul>
{% endif %}

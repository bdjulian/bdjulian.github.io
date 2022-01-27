---
---

<h1>Blog</h1>

<u1>
	{% for post in site.posts %}
	<li>
		<a href='{{ post.url | relative_url }}'>{{ post.title }} | {{ post.date | date_to_string: "ordinal", "US" }}</a>
	</li>
	{% endfor %}
</u1>

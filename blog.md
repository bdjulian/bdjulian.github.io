---
---

<h1>Blog</h1>

<u1>
	{% for post in site.posts %}
	<li>
		<a href='{{ post.url | relative_url }}'>{{ post.title }}</a>
	</li>
	{% endfor %}
</u1>


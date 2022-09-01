from django import template
from blog.models import Post

register = template.Library()

@register.inclusion_tag('blog/recent_tpl.html')
def get_recent():
    recent = Post.objects.all()[0:3]
    return {"recent":recent}

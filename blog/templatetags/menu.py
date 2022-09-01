from django import template
from blog.models import Category

register = template.Library()

@register.inclusion_tag('blog/menu_tpl.html')
def show_menu():
    categories = Category.objects.all()
    return {"categories": categories}

@register.inclusion_tag('blog/menu_tpl_mobile.html')
def show_menu_mobile():
    categories = Category.objects.all()
    return {"categories": categories}


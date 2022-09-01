from django import template
from blog.models import Single

register = template.Library()

@register.inclusion_tag('blog/footer_menu_tpl.html')
def show_footer_menu():
    singlePages = Single.objects.all()
    return {"singlePages": singlePages}

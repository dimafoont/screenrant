# from django import template
# from blog.models import Post
#
# register = template.Library()
#
# @register.inclusion_tag('blog/relevant_tpl.html')
# def get_relevant():
#     posts_count = Post.objects.count()
#     post1 = Post.objects.get(pk=posts_count)
#     post2 = Post.objects.get(pk=posts_count-1)
#     post3 = Post.objects.get(pk=posts_count-2)
#     post4 = Post.objects.get(pk=posts_count-3)
#     post5 = Post.objects.get(pk=posts_count-4)
#     return {"post1":post1, "post2":post2, "post3":post3, "post4":post4, "post5": post5}

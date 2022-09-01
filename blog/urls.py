from django.urls import path

from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<str:slug>/', PostsByCategory.as_view(), name='category'),
    path('post/<str:slug>/', GetPost.as_view(), name='post'),
    path('load/', load_more, name='load'),
    path('load_cat/', load_more_cat, name='load_cat'),
    path('<str:slug>', GetSinglePost.as_view(), name='single'),
    path('search/', Search.as_view(), name='search'),
]
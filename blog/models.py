from django.db import models
from django.urls import reverse_lazy
from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Published on')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('category', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']

    class MPTTMeta:
        order_insertion_by = ['title']


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Published on')
    photo = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
    views = models.IntegerField(default=0, verbose_name='Views')
    category = TreeForeignKey(Category, on_delete=models.PROTECT, related_name='posts')

    def __str__(self):
        return  self.title

    def get_absolute_url(self):
        return reverse_lazy('post', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ['-created_at']

class Single(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    content = models.TextField(blank=True)

    def __str__(self):
        return  self.title

    def get_absolute_url(self):
        return reverse_lazy('single', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'single-post'
        verbose_name_plural = 'single-posts'
        ordering = ['title']

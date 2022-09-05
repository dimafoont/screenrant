from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe
# from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin


from .models import *

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'

class CategoryAdmin(DraggableMPTTAdmin, admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    form = PostAdminForm
    save_as = True
    save_on_top = True
    list_display = ('id', 'title', 'slug', 'category', 'created_at', 'get_photo')
    list_display_links = ('title',)
    list_editable = ('created_at', 'category')
    list_filter = ('category',)
    readonly_fields = ('views', 'get_photo')
    fields = ('title', 'slug', 'category', 'content', 'photo', 'get_photo', 'views', 'created_at',)

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'

    get_photo.short_description = 'Photo'


class SinglePostAdmin(admin.ModelAdmin, PostAdminForm):
    form = PostAdminForm

# admin.site.register(CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Single, SinglePostAdmin)
admin.site.register(
    Category,
    CategoryAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
)

from django.contrib import admin

from .models import Category, Post


# for Configurations of model admins
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'tittle', 'description', 'url', 'add_date')
    search_fields = ('tittle', 'description')


class PostAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'tittle', 'category')
    search_fields = ('tittle',)
    list_filter = ('category',)
    list_per_page = 7

    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js', 'js/script.js',)


# Register your models here.

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

# 2:52:45

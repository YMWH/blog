from django.contrib import admin

# Register your models here.
from .models import Post, Category, Tag
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
    filter_horizontal = ('tags',)

class PostCategory(admin.ModelAdmin):
    list_display = ["id", "name"]

# 把新增的 PostAdmin 也注册进来
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
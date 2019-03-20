from django.contrib import admin

# Register your models here.
from .models import Course_Post, Course_title
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "name", 'create_time', 'modified_time', 'serial', 'course']

# 把新增的 PostAdmin 也注册进来
admin.site.register(Course_title, CourseAdmin)
admin.site.register(Course_Post, PostAdmin)

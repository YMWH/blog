from django.contrib import admin
from .models import Comment, CommentUsers, CommentCourse

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'users', 'created_time', 'post', 'floor', 'belong']

class Course(admin.ModelAdmin):
    list_display = ['id', 'users', 'created_time', 'coursePost',  'floor', 'belong']

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'state', 'powerDelete', 'powerChange']
# Register your models here.
admin.site.register(Comment, CommentAdmin)
admin.site.register(CommentUsers, UserAdmin)
admin.site.register(CommentCourse, Course)
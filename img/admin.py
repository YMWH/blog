from django.contrib import admin

# Register your models here.
from .models import courseImg

class courseImgAdmin(admin.ModelAdmin):
    list_display = ["id", "name", 'address', 'explain', 'course']

# 把新增的 PostAdmin 也注册进来
admin.site.register(courseImg, courseImgAdmin)

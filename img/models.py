from django.db import models

# Create your models here.
class courseImg(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    explain = models.CharField(max_length=200)
    title = models.CharField(max_length=100, default="",  null=True, blank=True)
    content = models.CharField(max_length=200, default="", null=True, blank=True)
    course = models.ForeignKey("Course.Course_title", null=True, blank=True)



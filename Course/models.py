from django.db import models

class Course_title(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
class Course_Post(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    create_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    serial = models.PositiveIntegerField(default=1)
    course = models.ForeignKey(Course_title)
    def __str__(self):
        return self.name
# Create your models here.

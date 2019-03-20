from django import template
from ..models import Course_title, Course_Post

register = template.Library()


@register.simple_tag
def get_title():
    return Course_title.objects.all()

@register.simple_tag
def get_recent_posts():
    return Course_Post.objects.all().order_by('-create_time')[:5]
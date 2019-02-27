# 自定义标签，simple_tag在django1.9版本后才支持
from ..models import Post, Category
from django import template

register = template.Library()

# 获取最新文章自定义标签
@register.simple_tag()#simple_tag在django1.9版本后才支持
def get_recent_posts(num=5):
    #获取最新的前五篇文章
    return Post.objects.all().order_by('-created_time')[:num]

# 归档自定义标签
@register.simple_tag()
def archives():
    # 获取文章创建时间，dates()会返回一个列表，第一个参数是获取创建时间的数值，第二个参数是精确到月份，第三个参数是倒序排列
    return Post.objects.dates('created_time', 'day', order = 'DESC')

# 自定义分类模板标签
@register.simple_tag()
def get_categories():
    return Category.objects.all()
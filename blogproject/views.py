from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Tag
from Course.models import Course_Post
from comments.forms import Commetforms
import markdown
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import time
# from django.db.models import Q
# Create your views here.

# 首页
def index(request):
    category_all = Category.objects.all()
    for category_all_id in category_all:
        Category.length = len(Post.objects.filter(category_id=category_all_id.id))
        Category.objects.filter(id = category_all_id.id).update(length = Category.length)
    post_list = Post.objects.all().order_by("-created_time")
    root = "base.html"
    contacts, page_object = paging(request, post_list)
    post_list = contacts.object_list
    tags_str = -1
    newYear = time.strftime('%Y',time.localtime(time.time()))
    return render(request, "blog/index.html", locals())

# 关于
def about(request):
    root = "base.html"
    return render(request, 'blog/about.html', locals())

# 联系
def contact(request):
    root = "base.html"
    return render(request, 'blog/contact.html', locals())

# 博客
def full_width(request):
    root = "base.html"
    return render(request, 'blog/full-width.html', locals())

# 详情页
def detail(request, pk):
    tags_str = request.path.find('post')
    # coursePost = get_object_or_404(Course_Post, pk=course_pk)
    post = get_object_or_404(Post, pk=pk)
    post.increase_views()
    post_tags = Tag.objects.filter(post=post)
    # post.body = markdown.markdown(post.body,
    #                               extensions=[
    #                                   'markdown.extensions.extra',
    #                                   'markdown.extensions.codehilite',
    #                                   'markdown.extensions.toc',
    #                               ])
    post, state = get_object(post)
    root = "base.html"
    form = Commetforms()
    comment_list = post.comment_set.all()
    context = {
        'post': post,
        'form': form,
        'comment_list': comment_list
    }

    return render(request, "blog/detail.html", locals())

# 归档
def archives(request, year, month, day):
    root = "base.html"
    tags_str = -1
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month,
                                    created_time__day=day
                                    ).order_by('-created_time')
    return render(request, 'blog/index.html', locals())

# 分类
def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by("-created_time")
    root = "base.html"
    tags_str = -1
    return render(request, "blog/index.html", locals())

# 页码
def paging(request, post_list):
    page_number = 3
    paginator = Paginator(post_list, page_number)
    page_num = request.GET.get("page")
    page_object = 1
    try:
        contacts = paginator.page(page_num)
        page_object = int(page_num)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return contacts, page_object

# 标签
def tags(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tags=tag)
    root = "base.html"
    return render(request, "blog/index.html", locals())

# 目录
def get_object(post):
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    post.body = md.convert(post.body)
    post.toc = md.toc
    testing = post.toc.find("li")
    if testing == -1:
        return post, 0
    else:
        return post, 1

# 搜索
# 方法一
# def search(request):
#     q = request.GET.get('q')
#     error_msg = ''
#     root = "base.html"
#     if not q:
#         error_msg = "请输入搜索信息"
#         return render(request, 'blog/index.html', locals())
#     post_list = Post.objects.filter(Q(title__icontains=q)|Q(body__icontains=q))
#     return render(request, 'blog/index.html', locals())

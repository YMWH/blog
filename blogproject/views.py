from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from comments.forms import Commetforms
import markdown
# Create your views here.
def index(request):
    post_list = Post.objects.all().order_by("-created_time")
    root = "base.html"
    return render(request, "blog/index.html", locals())
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    root = "base.html"
    form = Commetforms()
    comment_list = post.comment_set.all()
    context = {
        'post': post,
        'form': form,
        'comment_list': comment_list
    }
    return render(request, "blog/detail.html", locals())

def archives(request, year, month, day):
    root = "base.html"
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month,
                                    created_time__day=day
                                    ).order_by('-created_time')
    return render(request, 'blog/detail.html', locals())
def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    Post.objects.filter(category=cate).delete()
    post_list = Post.objects.filter(category=cate).order_by("-created_time")
    root = "base.html"
    return render(request, "blog/index.html", locals())
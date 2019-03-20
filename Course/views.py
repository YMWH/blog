from django.shortcuts import render
from .models import Course_Post
import time
import markdown
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
from comments.models import *
# Create your views here.

def index(request):
    # 获取远程连接的ip
    user_ip = request.environ["REMOTE_ADDR"]
    userData = CommentUsers.objects.filter(userIp=user_ip)
    newYear = time.strftime('%Y', time.localtime(time.time()))
    CourseRoot = 'courseBase.html'
    userName = ''
    if not userData:
        return render(request, 'Course/index.html', locals())
    else:
        if userData[0].state:
            userName = userData[0].name
            return render(request, 'Course/index.html', locals())
        else:
            return render(request, 'Course/index.html', locals())
def StartPage(request, pk):
    userName = ''
    post_list = Course_Post.objects.filter(course_id=pk).order_by('serial')
    post_value = post_list[0]
    CourseRoot = 'courseBase.html'
    post, state, newYear, userData, commentAllData = public(request,post_value)
    chapterUp = 0
    if len(post_list)>1:
        chapterDown = post_list[1].id
    else:
        chapterDown = 0
    if not userData:
        return render(request, 'Course/Course_details.html', locals())
    else:
        if userData[0].state:
            userName = userData[0].name
            return render(request, 'Course/Course_details.html', locals())
        else:
            return render(request, 'Course/Course_details.html', locals())
def Course_details(request, pk):
    userName = ''
    allList = []
    post_details = Course_Post.objects.filter(id=pk)
    allData = Course_Post.objects.filter(course_id=post_details[0].course_id).order_by('serial')
    for postData in allData:
        allList.append(postData)
    try:
        target = allList.index(post_details[0])
        if target > 0 and target < len(allList)-1:
            chapterUp = allList[target - 1].id
            chapterDown = allList[target + 1].id
        elif target == 0:
            chapterUp = 0
            if len(allList) > 1:
                chapterDown = allList[target + 1].id
            else:
                chapterDown = 0
        elif target == len(allList)-1:
            chapterUp = allList[target - 1].id
            chapterDown = 0
        CourseRoot = 'courseBase.html'
        post_value = post_details[0]
        post_id = post_value.course_id
        post_list = Course_Post.objects.filter(course_id=post_id).order_by('serial')
        post, state, newYear, userData, commentAllData = public(request, post_value)
        if not userData:
            return render(request, 'Course/Course_details.html', locals())
        else:
            if userData[0].state:
                userName = userData[0].name
                return render(request, 'Course/Course_details.html', locals())
            else:
                return render(request, 'Course/Course_details.html', locals())
    except:
        pass

def public(request, post_value):
    newYear = time.strftime('%Y',time.localtime(time.time()))
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        # 'markdown.extensions.toc',
        TocExtension(slugify=slugify),
    ])
    post_value.body = md.convert(post_value.body)
    post_value.toc = md.toc
    testing = post_value.toc.find("li")
    # 获取远程连接的ip
    user_ip = request.environ["REMOTE_ADDR"]
    userData = CommentUsers.objects.filter(userIp=user_ip)
    commentAllData = CommentCourse.objects.filter(coursePost_id=post_value.id).order_by("-created_time")
    if testing == -1:
        return post_value, 0, newYear, userData, commentAllData
    else:
        return post_value, 1, newYear, userData, commentAllData

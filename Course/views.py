from django.shortcuts import render
from .models import Course_Post, Course_title
import time
import markdown
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
from comments.models import *
from img.models import courseImg
# Create your views here.

def index(request):
    # 获取远程连接的ip
    # user_ip = request.environ["REMOTE_ADDR"]
    # userData = CommentUsers.objects.filter(userIp=user_ip)
    newYear = time.strftime('%Y', time.localtime(time.time()))
    CourseRoot = 'courseBase.html'
    userName = ''
    ico = courseImg.objects.filter(name='ico')[0]
    logo = courseImg.objects.filter(name='courseLogo')[0]
    nominate = courseImg.objects.filter(name="推荐")
    if not judgelogin(request):
        return render(request, 'Course/index.html', locals())
    else:
        userName = request.COOKIES.get('username')
        return render(request, 'Course/index.html', locals())
def StartPage(request, pk):
    userName = ''
    post_list = Course_Post.objects.filter(course_id=pk).order_by('serial')
    post_value = post_list[0]
    CourseRoot = 'courseBase.html'
    post, state, newYear, commentParentList, commentChildList, userData = public(request,post_value)
    chapterUp = 0
    if len(post_list)>1:
        chapterDown = post_list[1].id
    else:
        chapterDown = 0
    if not judgelogin(request):
        return render(request, 'Course/Course_details.html', locals())
    else:
        userName = request.COOKIES.get('username')
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
        post, state, newYear, commentParentList, commentChildList, userData = public(request, post_value)

        if not judgelogin(request):
            return render(request, 'Course/Course_details.html', locals())
        else:
            userName = request.COOKIES.get('username')
            return render(request, 'Course/Course_details.html', locals())
    except:
        pass

def public(request, post_value):
    commentParentList = []
    commentChildList = []
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
    # user_ip = request.environ["REMOTE_ADDR"]
    # userData = CommentUsers.objects.filter(userIp=user_ip)
    userData = CommentUsers.objects.all()
    commentAllData = CommentCourse.objects.filter(coursePost_id=post_value.id).order_by("-created_time")
    for commentData in commentAllData:
        if commentData.floor == 0:
            commentParentList.append(commentData)
        else:
            commentChildList.append(commentData)
    if testing == -1:
        state = 0
    else:
        state = 1
    return post_value, state, newYear, commentParentList, commentChildList, userData


def judgelogin(request):
    user_ip = request.environ["REMOTE_ADDR"]
    if request.COOKIES.get('login') != "True":
    # if request.session.get('is_login') != True:
        request.session['redrect'] = True
        CommentUsers.objects.filter(userIp=user_ip).update(state=False)
        return False
    return True


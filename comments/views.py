from django.shortcuts import render, get_object_or_404, redirect
from .models import CommentUsers, CommentCourse
from .forms import Commetforms
from blogproject.models import Post
from Course.models import Course_Post
from django.http import HttpResponse
import json
from datetime import datetime

# Create your views here.

# 评论
def criticism(request):
    if request.is_ajax() and request.method == 'POST':
        textAll = request.POST

        usertext = textAll['catalog']#获取评论内容
        userFloor = int(textAll['floor'])#获取楼层值
        userParentId = int(textAll['parentId'])#获取楼主id
        userChildId = int(textAll['childId'])#获取楼层回复的id
        userName = textAll["username"]#获取评论的人

        if userFloor == 0:
            userParentId = 0
            userChildId = 0
        elif userFloor == 1:
            userChildId = userParentId
        elif userFloor == 2:
            pass

        website = request.environ['HTTP_REFERER']#获取完整的地址
        weburl = request.environ['HTTP_ORIGIN']#获取http://xxxxxx
        user_ip = request.environ["REMOTE_ADDR"]#获取网页ip
        webname = website[len(weburl)+1:]
        webClassify = webname.find("StartPage")
        userAllData = CommentUsers.objects.filter(name=userName)
        userData = get_object_or_404(CommentUsers, pk = userAllData[0].id)
        post = ''
        article = ''
        if webClassify != -1:
            webIdData = webname[len("StartPage")+1:]
            if webIdData.find("/") != -1:
                webId = webIdData[0:webIdData.find("/")]
            else:
                webId = webIdData[0:]
            article = Course_Post.objects.all().filter(course_id = webId).order_by("serial")[0].id
            post = get_object_or_404(Course_Post, pk = article)
        elif webname.find("CourseDetails") != -1:
            webIdData = webname[len("CourseDetails") + 1:]
            if webIdData.find("/") != -1:
                webId = webIdData[0:webIdData.find("/")]
            else:
                webId = webIdData[0:]
            article = webId
            post = get_object_or_404(Course_Post, pk = article)
        comment = CommentCourse(text=usertext, floor=userFloor, belong=userParentId, Native=userChildId)
        comment.coursePost = post
        comment.users = userData
        comment.save()
        commentData = CommentCourse.objects.filter(coursePost_id=article, users_id=userAllData[0].id).order_by("-created_time")[0]
        name = commentData.users.name
        body = commentData.text
        date = commentData.created_time.strftime("%Y-%m-%d %H:%M:%S")
        newId = commentData.id
        dataList = [name, body, date, newId]
        data = json.dumps(dataList)
        return HttpResponse(data)

# 注销
def cancel(request):
    if judgelogin(request):
        user_ip = request.environ["REMOTE_ADDR"]
        userData = CommentUsers.objects.filter(userIp=user_ip)
        if request.is_ajax() and request.method == 'POST':
            name = request.POST.getlist('name')[0]
            userName = CommentUsers.objects.filter(name=name)[0]
            if userData:
                if userName.userIp == userData[0].userIp:
                    CommentUsers.objects.filter(userIp=user_ip).update(state=False)
                    data = json.dumps([0])

                    response = HttpResponse(data)
                    response.set_cookie('login', False)
                    return response

# 注册
def register(request):
    # 注册数据格式：["register", "注册状态码", "邮箱状态码"]
    # register:标记该数据为注册反馈数据
    # 注册状态码:如果注册成功，返回1;
    #               如果重复注册，返回0;
    #               注册失败，返回-1
    # 邮箱状态码:如果该邮箱第一次注册，返回1，否则返回0，且提示注册失败，邮箱均返回0
    if request.is_ajax() and request.method == 'POST':
        name = request.POST.getlist('userName')[0]
        password = request.POST.getlist('password')[0]
        mail = request.POST.getlist('mailbox')[0]
        user = CommentUsers.objects.filter(name=name)
        userEmail = CommentUsers.objects.filter(email=mail)
        if not user:
            if not userEmail:
                user = CommentUsers(name=name, passWord=password, email=mail)
                user.save()
                registerData = ["register", 1, 1]
                data = json.dumps(registerData)#"注册成功"
                return HttpResponse(data)
            else:
                registerData = ["register", -1, 0]
                data = json.dumps(registerData)#"该邮箱已经注册过，请用其他邮箱注册"
                return HttpResponse(data)
        else:
            registerData = ["register", 0, 0]
            data = json.dumps(registerData)#"账号已经存在，请重新注册"
            return HttpResponse(data)

# cookie
def judgelogin(request):
    if request.COOKIES.get('login') != "True":
    # if request.session.get('is_login') != True:
        request.session['redrect'] = True
        return False
    return True

# 登录
def login(request):
    # 返回数据为：["login", "反馈登录状态"，"登录状态码"，"用户名"];
    # login:标记该数据为登录数据
    # 反馈登录状态:如果没有注册，返回数据为0;
    #               如果密码错误，返回数据为-1;
    #               如果重复登录，返回数据为-2;
    #               如果登录成功，返回数据为1;
    # 登录状态码:分为离线和在线两个状态
    #               离线状态为0;
    #               在线状态为1;
    #               不管在线状态只能维持30min，均会自动下线，不管有无数据传输;
    # 用户名:
    #               如果无账号，返回0;
    #               如果有账号，返回该用户名;

    if request.is_ajax() and request.method == 'POST':
        name = request.POST.getlist('userName')[0]
        password = request.POST.getlist('password')[0]
        allData = CommentUsers.objects.all().filter(name=name)
        user_ip = request.environ["REMOTE_ADDR"]
        if not allData:
            loginData = ["login", 0, 0, 0]
            data = json.dumps(loginData) #"该账户不存在，请先注册"
            return HttpResponse(data)
        else:
            allData = allData[0]
            if allData.passWord == password:
                if allData.state:
                    loginData = ["login", -2, allData.state, allData.name]
                    data = json.dumps(loginData)#"重复登录"
                    return HttpResponse(data)
                else:
                    CommentUsers.objects.filter(id=allData.id).update(state=True, userIp=user_ip)
                    allData = CommentUsers.objects.all().filter(name=name)[0]
                    # CommentUsers.objects.filter(id=allData.id).update(userIp=user_ip)
                    # session
                    # request.session["is_login"] = True
                    # request.session["user_id"] = allData.id
                    # request.session["user_name"] = allData.name

                    # COOKIE
                    loginData = ["login", 1, allData.state, allData.name]
                    data = json.dumps(loginData)  # "登录成功"

                    response = HttpResponse(data)
                    response.set_cookie('login', True, max_age=1800)
                    response.set_cookie('username', allData.name)
                    return response
            else:
                loginData = ["login", -1, allData.state, allData.name]
                data = json.dumps(loginData)#"密码错误"
                return HttpResponse(data)

def post_comment(request, pk):
    post = get_object_or_404(Post, pk = pk)
    if request.method == 'POST':
        form = Commetforms(request.POST)
        if form.is_valid():
            # commit=False 的作用是仅仅利用表单的数据生成 Comment 模型类的实例，但还不保存评论数据到数据库。
            comment = form.save(commit=False)
            # 关联评论和被评论的文章
            comment.post = post
            comment.save()
            # 重定向到 post 的详情页，实际上当 redirect 函数接收一个模型的实例时，它会调用这个模型实例的 get_absolute_url 方法，
            # 然后重定向到 get_absolute_url 方法返回的 URL。
            return redirect(post)
        else:
            # 检查到数据不合法，重新渲染详情页，并且渲染表单的错误。
            # 因此我们传了三个模板变量给 detail.html，
            # 一个是文章（Post），一个是评论列表，一个是表单 form
            # 注意这里我们用到了 post.comment_set.all() 方法，
            # 这个用法有点类似于 Post.objects.all()
            # 其作用是获取这篇 post 下的的全部评论，
            # 因为 Post 和 Comment 是 ForeignKey 关联的，
            # 因此使用 post.comment_set.all() 反向查询全部评论。
            comment_list = post.comment_set.all()
            context = {
                'post':post,
                'form':form,
                'comment_list':comment_list
            }
            return render(request, 'blog/detail.html', context=context)
    return redirect(post)
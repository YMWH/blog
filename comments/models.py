from django.db import models

# Create your models here.
class CommentUsers(models.Model):
    # '''
    #     name:用户名
    #     passWord:用户密码
    #     email:用户邮箱，可以找回密码用
    #     phoneNumber:手机号
    #     state:登录状态
    #     powerDelete:删除个人资料的权力
    #     powerChange:修改个人资料的权力
    #     注意：更改权和删除权仅仅只是针对用户自己有效，对于其他用户无效
    # '''
    name = models.CharField(max_length=100)
    passWord = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    # phoneNumber = models.PositiveIntegerField()
    # joinDate = models.DateTimeField(blank=True, null=True)
    lastTime = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    state = models.BooleanField(default=False)
    powerDelete = models.BooleanField(default=True)
    powerChange = models.BooleanField(default=True)
    userIp = models.CharField(max_length=100, default='')
    def __str__(self):
        return self.name

class Comment(models.Model):
    # '''
    #     text:评论内容
    #     created_time:评论时间
    #     floor:评论楼层，总共有三级评论，一级为初始楼层
    #     belong:从二级开始，由该字段决定回复属于的初始评论
    #     post:如果字段值不为0，那么该条评论属于博客页面
    #     coursePost:如果字段值不为0，那么该条评论属于教程页面
    #     users:记录该条评论属于哪个用户
    # '''

    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    floor = models.PositiveIntegerField(default=0)
    belong = models.PositiveIntegerField(default=0)
    post = models.ForeignKey('blogproject.Post')
    users = models.ForeignKey(CommentUsers,default=50)
    def __str__(self):
        return self.text[:20]
class CommentCourse(models.Model):
    # '''
    #     text:评论内容
    #     created_time:评论时间
    #     floor:评论楼层，总共有三级评论，一级为初始楼层
    #     belong:从二级开始，由该字段决定回复属于的初始评论
    #     post:如果字段值不为0，那么该条评论属于博客页面
    #     coursePost:如果字段值不为0，那么该条评论属于教程页面
    #     users:记录该条评论属于哪个用户
    # '''
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    floor = models.PositiveIntegerField(default=0)
    belong = models.PositiveIntegerField(default=0)
    coursePost = models.ForeignKey('Course.Course_Post')
    users = models.ForeignKey(CommentUsers, default=50)
    def __str__(self):
        return self.text[:20]

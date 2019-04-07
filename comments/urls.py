from . import views
from django.conf.urls import url

app_name = "comments"

urlpatterns = [
    url(r'^comments/post/(?P<pk>[0-9]+)/$', views.post_comment, name = "post"),
    url(r'^comments/login/$', views.login, name = "login"),
    url(r'^comments/register/$', views.register, name = "register"),
    url(r'^comments/cancel/$', views.cancel, name = "cancel"),
    url(r'^comments/course/criticism/$', views.criticism, name = "criticism"),
    url(r'^comments/course/criticism/firstChild/$', views.criticism, name = "criticism"),
    # url(r'^comments/course/criticism/secondChild/$', views.criticism, name = "criticism"),
]
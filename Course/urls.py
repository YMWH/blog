from django.conf.urls import url
from . import views
from .feeds import AllPostsRssFeed

app_name = "Course"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^index/$', views.index, name="index"),
    url(r'^StartPage/(?P<pk>[1-9]+)/$', views.StartPage, name='StartPage'),
    url(r'^CourseDetails/(?P<pk>[1-9]+)/$', views.Course_details, name='CourseDetails'),
    url(r'^Course/all/rss/$', AllPostsRssFeed(), name='CourseRss'),
]

from django.conf.urls import url
from . import views

app_name = 'blogproject'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name = 'index'),
    url(r'^about/$', views.about, name = 'about'),
    url(r'^contact/$', views.contact, name = 'contact'),
    url(r'^full_width/$', views.full_width, name = 'full_width'),
    url(r'^blog/index.html$', views.index, name = 'index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/(?P<day>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
    url(r'^tags/(?P<pk>[0-9]+)/$', views.tags, name='tags'),
    # url(r'^search/$', views.search, name='search'),
]
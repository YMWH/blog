from . import views
from django.conf.urls import url

app_name = "comments"

urlpatterns = [
    url(r'^comments/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name = "comments"),
]
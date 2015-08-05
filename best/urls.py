from django.conf.urls import url
from best import views

urlpatterns = [
    url(r'^api/groups/(?P<pk>[0-9]+)/$', views.group_detail),
]

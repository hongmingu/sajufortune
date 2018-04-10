from django.urls import path, re_path
from . import views

app_name = 'celebrity'

# 여기는 domain.com/ 을 다루는 데에 주로 쓰일 것
# I do not want to use project_name/urls.py except include

urlpatterns = [
    # re_path(r'^password/change/$', views.main_create_log_in, name='main'),
    re_path(r'^profile/(?P<lang>ara|chi|eng|por|spa)/(?P<num>\d+)/$', views.profile_celeb, name='profile'),
    re_path(r'^list/(?P<lang>ara|chi|eng|por|spa)/(?P<page>\d+)/$', views.list_celeb, name='list'),
    re_path(r'^day/(?P<lang>ara|chi|eng|por|spa)/$', views.day_celeb, name='day'),
]

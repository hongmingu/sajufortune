from django.urls import path, re_path
from . import views
from django.views.decorators.cache import cache_page, never_cache

app_name = 'post'

# 여기는 domain.com/ 을 다루는 데에 주로 쓰일 것
# I do not want to use project_name/urls.py except include

urlpatterns = [
    # re_path(r'^password/change/$', views.main_create_log_in, name='main'),
    re_path(r'^list/(?P<lang>ara|chi|eng|por|spa)/(?P<page>\d+)/$', cache_page(0)(views.post_list), name='list'),
    re_path(r'^detail/(?P<lang>ara|chi|eng|por|spa)/(?P<num>\d+)/$', cache_page(0)(views.post_detail), name='detail'),
]

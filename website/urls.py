from django.urls import re_path
from django.views.decorators.cache import cache_page

from . import views

app_name = 'website'

# 여기는 domain.com/ 을 다루는 데에 주로 쓰일 것
# I do not want to use project_name/urls.py except include

urlpatterns = [

    re_path(r'^$', cache_page(60 * 15)(views.main), name='main'),
    re_path(r'^(?P<lang>ara|chi|eng|por|spa)/$', cache_page(60 * 15)(views.main_lang), name='main_lang'),
    re_path(r'^day/(?P<lang>ara|chi|eng|por|spa)/$', cache_page(60 * 15)(views.day), name='day'),

    re_path(r'^about/(?P<lang>ara|chi|eng|por|spa)/$', cache_page(60 * 60 * 12)(views.about), name='about'),
    re_path(r'^ping/', cache_page(60 * 60 * 24)(views.ping_test), name='ping_test'),
]

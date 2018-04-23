from django.urls import path, re_path
from django.views.generic import TemplateView

from . import views
from django.views.decorators.cache import cache_page, never_cache

app_name = 'website'

# 여기는 domain.com/ 을 다루는 데에 주로 쓰일 것
# I do not want to use project_name/urls.py except include

urlpatterns = [

    re_path(r'^$', cache_page(0)(views.main), name='main'),
    re_path(r'^(?P<lang>ara|chi|eng|por|spa)/$', cache_page(60 * 15)(views.main_lang), name='main_lang'),

    re_path(r'^about/(?P<lang>ara|chi|eng|por|spa)/$', cache_page(60 * 60 * 12)(views.about), name='about'),

    re_path(r'^day/(?P<lang>ara|chi|eng|por|spa)/$', cache_page(60 * 10)(views.day), name='day'),

    re_path(r'^test2/', views.test2, name='test2'),
    re_path(r'^test/', views.test, name='test'),
]


'''
If your url is something like domain/search/?q=haha, Then you would use request.GET.get('q', '').

q is the parameter you want, And '' is the default value if q isn't found.

If you are instead just configuring your URLconf, Then your captures from the regex are passed to the function as arguments (or named arguments).

Such as:

(r'^user/(?P<username>\w{0,50})/$', views.profile_page,),
Then in your views.py you would have

def profile_page(request, username):
    # Rest of the method
'''

# 웹소켓 되면
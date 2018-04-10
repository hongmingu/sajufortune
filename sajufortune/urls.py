"""laymei URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
# 이 아래부분 미디어 파일 디벨롭모드에서 쓰기 위해 필요
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include('website.urls')),
    re_path(r'^dayoverall/', include('dayoverall.urls')),
    re_path(r'^daywork/', include('daywork.urls')),
    re_path(r'^daylove/', include('daylove.urls')),
    re_path(r'^daymoney/', include('daymoney.urls')),
    re_path(r'^dayrelationships/', include('dayrelationships.urls')),
    re_path(r'^dayemotion/', include('dayemotion.urls')),
    re_path(r'^post/', include('post.urls')),
    re_path(r'^celeb/', include('celebrity.urls')),

]

#이 아래 부분 미디어 파일 디벨롭 모드에서 쓰기 위해 필요
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''
    url(r'^accounts/', include('dayoverall.urls', namespace='accounts')),
    url(r'base_test/$', TemplateView.as_view(template_name='base_test.html')),
'''
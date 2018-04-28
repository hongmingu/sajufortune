from django.contrib.sitemaps import views as sitemap_views
from django.urls import re_path, path
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView

from website.sitemaps import sitemaps
from . import views

app_name = 'website'

urlpatterns = [

    re_path(r'^$', cache_page(60 * 15)(views.main), name='main'),
    re_path(r'^(?P<lang>ara|chi|eng|por|spa)/$', cache_page(60 * 15)(views.main_lang), name='main_lang'),
    re_path(r'^day/(?P<lang>ara|chi|eng|por|spa)/$', cache_page(60 * 15)(views.day), name='day'),

    re_path(r'^about/(?P<lang>ara|chi|eng|por|spa)/$', cache_page(60 * 60 * 12)(views.about), name='about'),
    re_path(r'^ping/$', cache_page(60 * 60 * 24)(views.ping_test), name='ping_test'),

    re_path(r'^robots\.txt$', TemplateView.as_view(template_name="snippet/others/robots.txt", content_type="text/plain"), name="robots"),

    path('sitemap.xml', sitemap_views.index, {'sitemaps': sitemaps, 'sitemap_url_name': 'website:sitemaps'}),
    path('sitemap-<section>.xml', sitemap_views.sitemap, {'sitemaps': sitemaps},
         name='sitemaps'),

]

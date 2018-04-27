from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from celebrity.models import *
from post.models import *
from django.core.cache import cache
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



class PostArabicSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return PostArabic.objects.all()

    def lastmod(self, obj):
        return obj.updated

class PostChineseSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return PostChinese.objects.all()

    def lastmod(self, obj):
        return obj.updated

class PostEnglishSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return PostEnglish.objects.all()

    def lastmod(self, obj):
        return obj.updated

class PostPortugueseSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return PostPortuguese.objects.all()

    def lastmod(self, obj):
        return obj.updated

class PostSpanishSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return PostSpanish.objects.all()

    def lastmod(self, obj):
        return obj.updated


class PostListSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0

    def items(self):
        cache_post_queryset = cache.get('post_objects_all_order_by_created')
        if cache_post_queryset is not None:
            post_queryset = cache_post_queryset
        else:
            post_queryset = Post.objects.all().order_by('-created')
            cache.set('post_objects_all_order_by_created', post_queryset, timeout=60 * 60)

        post_paginator = Paginator(post_queryset, 10)
        pages_number = post_paginator.num_pages
        lang_list = ['ara', 'chi', 'eng', 'por', 'spa']
        item_list = []
        for i in range(len(lang_list)):
            for i_two in range(pages_number):
                item_list.append({lang_list[i]: i_two})

        return item_list

    def location(self, item):
        return reverse('celebrity:list', kwargs={'lang': next(iter(item)), 'page': item.get(next(iter(item)))})



class CelebrityArabicSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return CelebrityArabic.objects.all()

    def lastmod(self, obj):
        return obj.updated


class CelebrityChineseSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return CelebrityChinese.objects.all()

    def lastmod(self, obj):
        return obj.updated


class CelebrityEnglishSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return CelebrityEnglish.objects.all()

    def lastmod(self, obj):
        return obj.updated


class CelebrityPortugueseSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return CelebrityPortuguese.objects.all()

    def lastmod(self, obj):
        return obj.updated


class CelebritySpanishSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return CelebritySpanish.objects.all()

    def lastmod(self, obj):
        return obj.updated


class CelebrityListSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0

    def items(self):
        cache_celeb_objects_all = cache.get('celebrity_objects_all')
        if cache_celeb_objects_all is not None:
            celeb_all = cache_celeb_objects_all
        else:
            celeb_all = Celebrity.objects.all()
            cache.set('celebrity_objects_all', celeb_all, timeout=60 * 60)

        celeb_paginator = Paginator(celeb_all, 10)
        pages_number = celeb_paginator.num_pages
        lang_list = ['ara', 'chi', 'eng', 'por', 'spa']
        item_list = []
        for i in range(len(lang_list)):
            for i_two in range(pages_number):
                item_list.append({lang_list[i]: i_two})
        return item_list

    def location(self, item):
        return reverse('celebrity:list', kwargs={'lang': next(iter(item)), 'page': item.get(next(iter(item)))})


class CelebrityListTextSitemap(Sitemap):
    changefreq = "weeekly"
    priority = 0.8

    def items(self):
        return ['ara', 'chi', 'eng', 'por', 'spa']

    def location(self, item):
        return reverse('celebrity:list_text', kwargs={'lang': item})


class MainSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return ['website:main']

    def location(self, item):
        return reverse(item)


class Main_LangSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return ['ara', 'chi', 'eng', 'por', 'spa']

    def location(self, item):
        return reverse('website:main_lang', kwargs={'lang': item})


class AboutSitemap(Sitemap):
    changefreq = "weeekly"
    priority = 0.8

    def items(self):
        return ['ara', 'chi', 'eng', 'por', 'spa']

    def location(self, item):
        return reverse('website:about', kwargs={'lang': item})

sitemaps = {
    'postarabic': PostArabicSitemap,
    'postenglish': PostEnglishSitemap,
    'postchinese': PostChineseSitemap,
    'postportuguese': PostPortugueseSitemap,
    'postspanish': PostSpanishSitemap,
    'celebrityarabic': CelebrityArabicSitemap,
    'celebritychinese': CelebrityChineseSitemap,
    'celebrityenglish': CelebrityEnglishSitemap,
    'celebrityportuguese': CelebrityPortugueseSitemap,
    'celebrityspanish': CelebritySpanishSitemap,
    'main': MainSitemap,
    'main_lang': Main_LangSitemap,
    'celeb_list': CelebrityListSitemap,
    'celeb_list_text': CelebrityListTextSitemap,
    'post_list': PostListSitemap,
    'about': AboutSitemap,
}
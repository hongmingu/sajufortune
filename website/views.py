from django.urls import reverse
from django.shortcuts import redirect

from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from post.models import Post
from website.utils import *
from django.core.cache import cache

from celebrity.models import Celebrity

from website.utils import get_day_fortune_model_by_index


def test2(request):
    if request.method == "POST":
        pass
    else:
        # cache_data = cache.get_or_set('render', None)
        return render(request, 'website/main/test2.html')


def test(request):
    if request.method == "POST":
        pass
    else:
        # cache_data = cache.get_or_set('render', None)
        return render(request, 'website/main/test.html')
        # 각각 div 놓고 거기에 데이터까지 준 다음에 그걸로 따로 ajax 통신해서 각자 데이터 가져가게끔 
        # if cache_data is None:
        #     rendered_data = render(request, 'website/main/test.html')
        #     cache.set('render', rendered_data)
        #     return rendered_data
        # else:
        #     return cache_data

        # get_data = request.GET.get('q', 'default_value')
        # get_cache = cache.get_or_set('posts'+get_data, get_data)
        #
        # answer = {'q': get_data}
        # return render(request, 'post/not_exist_post_default.html', {'answer': answer})

'''
class Post(models.Model):  
    ... # 생략
    def save(self, *args, **kwargs):
        cache.delete('posts')
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        cache.delete('posts')
        super().delete(*args, **kwargs)
        
        # Good
entry.blog_id
# DB에 접속
e = Entry.objects.get(id=5)

# 관련된 Blog 객체를 가져오기 위해 DB에 한번 더 접속
b = e.blog

# select_related을 사용
# DB에 접속
e = Entry.objects.select_related('blog').get(id=5)

# 이미 위에서 관련된 Blog객체들을 가져왔기 때문에 DB에 접속하지 않음
b = e.blog
# Bad
entry.blog.id

# Good
my_band.members.add(me, my_friend)

# Bad
my_band.members.add(me)
my_band.members.add(my_friend)

render 값을 cache할 수 있는가?
'''


def day(request, lang):
    if request.method == "GET":
        birthday_year_raw = request.GET.get('by', None)
        birthday_month_raw = request.GET.get('bm', None)
        birthday_day_raw = request.GET.get('bd', None)
        target_year_raw = request.GET.get('ty', None)
        target_month_raw = request.GET.get('tm', None)
        target_day_raw = request.GET.get('td', None)

        cache_day = cache.get('dayall' + lang +
                              birthday_year_raw + birthday_month_raw + birthday_day_raw +
                              target_year_raw + target_month_raw + target_day_raw)

        if cache_day is not None:
            return cache_day
        else:
            if birthday_year_raw is None or birthday_month_raw is None or birthday_day_raw is None \
                    or target_year_raw is None or target_month_raw is None or target_day_raw is None:
                # 제공되지 않은 값이 있을 경우
                return render(request, '404.html', )

            try:
                birthday_year = int(birthday_year_raw, 16)
                birthday_month = int(birthday_month_raw, 16)
                birthday_day = int(birthday_day_raw, 16)
                target_year = int(target_year_raw, 16)
                target_month = int(target_month_raw, 16)
                target_day = int(target_day_raw, 16)
            except ValueError:
                # 값이 제대로 변형되지 않은 경우
                return render(request, '404.html', )

            if not validate_date(birthday_year, birthday_month, birthday_day, target_year, target_month, target_day):
                # 값이 변형되었더라도 제대로 된 기간을 제시하지 않은 경우
                return render(request, '404.html', )

            result_num = get_result_num(birthday_year, birthday_month, birthday_day,
                                        target_year, target_month, target_day)

            overall_num = get_overall_num(result_num)
            emotion_num = get_emotion_num(result_num)
            love_num = get_love_num(result_num)
            money_num = get_money_num(result_num)
            relationships_num = get_relationships_num(result_num)
            work_num = get_work_num(result_num)

            num_list = [overall_num, emotion_num, love_num, money_num, relationships_num, work_num]

            cache_overall = cache.get('day' + '0' + ':' + overall_num)
            cache_emotion = cache.get('day' + '1' + ':' + emotion_num)
            cache_love = cache.get('day' + '2' + ':' + love_num)
            cache_money = cache.get('day' + '3' + ':' + money_num)
            cache_relationships = cache.get('day' + '4' + ':' + relationships_num)
            cache_work = cache.get('day' + '5' + ':' + work_num)

            cache_list = [cache_overall, cache_emotion, cache_love, cache_money, cache_relationships, cache_work]

            length_cache_list = len(cache_list)
            range_cache_list = range(length_cache_list)

            for i in range_cache_list:
                if cache_list[i] is None:
                    try:
                        result = get_day_fortune_model_by_index(i).objects.get(pk=num_list[i])
                    except get_day_fortune_model_by_index(i).DoesNotExist:
                        result = None
                    cache.set('day' + str(i) + ':' + num_list[i], result, timeout=60*60*24)
                    cache_list[i] = result

            birthday_dict = {
                'year': birthday_year,
                'month': birthday_month,
                'day': birthday_day
            }
            target_dict = {
                'year': target_year,
                'month': target_month,
                'day': target_day
            }

            cache_celeb_queryset = cache.get('celebrity_objects_all')
            if cache_celeb_queryset is not None:
                celeb_list = cache_celeb_queryset.order_by('?')
            else:
                celeb_queryset = Celebrity.objects.all()
                cache.set('celebrity_objects_all', celeb_queryset, timeout=60*60)
                celeb_list = celeb_queryset.order_by('?')

            celeb_paginator = Paginator(celeb_list, 2)
            try:
                other_celebs = celeb_paginator.page(1)
            except EmptyPage:
                other_celebs = celeb_paginator.page(celeb_paginator.num_pages)

            template = switch_day_template_by_lang(lang)
            render_day = render(request, template, {'lang': lang,
                                                    'birthday': birthday_dict,
                                                    'target': target_dict,
                                                    'other_celebs': other_celebs,
                                                    'overall': cache_list[0],
                                                    'emotion': cache_list[1],
                                                    'love': cache_list[2],
                                                    'money': cache_list[3],
                                                    'relationships': cache_list[4],
                                                    'work': cache_list[5], })

            cache.set('dayall' + lang +
                              birthday_year_raw + birthday_month_raw + birthday_day_raw +
                              target_year_raw + target_month_raw + target_day_raw, render_day, timeout=60*15)
            return render_day
    else:
        return JsonResponse({'Hello': 'You\'ve got wrong access! may god bless you.'})


def main(request):
    if request.method == "GET":

        cache_main = cache.get('main')
        if cache_main is not None:
            return cache_main
        else:
            cache_post_queryset = cache.get('post_objects_all_order_by_created')
            if cache_post_queryset is not None:
                post_queryset = cache_post_queryset
            else:
                post_queryset = Post.objects.all().order_by('-created')
                cache.set('post_objects_all_order_by_created', post_queryset, timeout=60*60)

            post_list = post_queryset
            post_paginator = Paginator(post_list, 10)
            try:
                posts = post_paginator.page(1)
            except PageNotAnInteger:
                posts = post_paginator.page(1)
            except EmptyPage:
                posts = post_paginator.page(post_paginator.num_pages)
            render_main = render(request, 'website/main/main_eng.html', {'posts': posts,
                                                                         'lang': 'eng'})
            cache.set('main', render_main, timeout=60*15)
            return render_main

    else:
        return JsonResponse({'Hello': 'You\'ve got wrong access! may god bless you.'})


def main_lang(request, lang):
    if request.method == "GET":

        if lang == 'eng':
            return redirect(reverse('website:main'))
        cache_main_lang = cache.get('main_lang' + lang)
        if cache_main_lang is not None:
            return cache_main_lang
        else:
            template = switch_main_lang_template_by_lang(lang)

            cache_post_queryset = cache.get('post_objects_all_order_by_created')

            if cache_post_queryset is not None:
                post_queryset = cache_post_queryset
            else:
                post_queryset = Post.objects.all().order_by('-created')
                cache.set('post_objects_all_order_by_created', post_queryset, timeout=60*60)

            post_list = post_queryset

            post_paginator = Paginator(post_list, 10)
            try:
                posts = post_paginator.page(1)
            except PageNotAnInteger:
                posts = post_paginator.page(1)
            except EmptyPage:
                posts = post_paginator.page(post_paginator.num_pages)

            rendered_data = render(request, template, {'posts': posts, 'lang': lang})
            cache.set('main_lang' + lang, rendered_data, 60 * 15)
            return rendered_data
    else:
        return JsonResponse({'Hello': 'You\'ve got wrong access! may god bless you.'})


def about(request, lang):
    if request.method == "GET":
        cache_about = cache.get('about' + lang)
        if cache_about is not None:
            return cache_about
        else:
            template = switch_about_template_by_lang(lang)
            render_about = render(request, template, {'lang': lang})
            cache.set('about' + lang, render_about, timeout=60 * 60 * 12)
            return render_about
    else:
        return JsonResponse({'Hello': 'You\'ve got wrong access! may god bless you.'})



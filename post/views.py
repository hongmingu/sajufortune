from django.core.cache import cache
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.shortcuts import render

from post.models import Post
from post.utils import *
from website.utils import *


# Create your views here.


def post_detail(request, num, lang):
    if request.method == "GET":

        cache_post_detail = cache.get('post_detail' + lang + num)

        if cache_post_detail is not None:
            return cache_post_detail

        else:
            cache_post_objects_get_num = cache.get('post_objects_get_num'+num)
            if cache_post_objects_get_num is not None:
                post = cache_post_objects_get_num
            else:
                try:
                    post = Post.objects.get(pk=num)
                except Post.DoesNotExist:
                    return render(request, '404.html', )
                cache.set('post_objects_get_num'+num, post, timeout=60*60)

            birthday_year_raw = post.celebrity.birthday_year
            birthday_month_raw = post.celebrity.birthday_month
            birthday_day_raw = post.celebrity.birthday_day
            target_year_raw = post.target_year
            target_month_raw = post.target_month
            target_day_raw = post.target_day
            if birthday_year_raw is None or birthday_month_raw is None or birthday_day_raw is None \
                    or target_year_raw is None or target_month_raw is None or target_day_raw is None:
                # 제공되지 않은 값이 있을 경우
                return render(request, '404.html', )

            try:
                birthday_year = int(post.celebrity.birthday_year)
                birthday_month = int(post.celebrity.birthday_month)
                birthday_day = int(post.celebrity.birthday_day)
                target_year = int(post.target_year)
                target_month = int(post.target_month)
                target_day = int(post.target_day)
            except ValueError:
                return render(request, '404.html')

            if not validate_date(birthday_year, birthday_month, birthday_day, target_year, target_month, target_day):
                # 값이 변형되었더라도 제대로 된 기간을 제시하지 않은 경우
                return render(request, '404.html',)

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

            cache_post_queryset = cache.get('post_objects_all_exclude'+num)

            if cache_post_queryset is not None:
                post_queryset = cache_post_queryset
            else:
                post_queryset = Post.objects.all().exclude(pk=num)
                cache.set('post_objects_all_exclude'+num, post_queryset, timeout=60*60)

            post_all = post_queryset.order_by('?')
            post_paginator = Paginator(post_all, 2)

            other_posts = post_paginator.page(1)
            template = switch_post_detail_template_by_lang(lang)

            render_post_detail = render(request, template, {'post': post,
                                              'other_posts': other_posts,
                                              'lang': lang,
                                              'birthday': birthday_dict,
                                              'target': target_dict,
                                              'overall': cache_list[0],
                                                'emotion': cache_list[1],
                                                'love': cache_list[2],
                                                'money': cache_list[3],
                                                'relationships': cache_list[4],
                                                'work': cache_list[5], })
            cache.set('post_detail' + lang + num, render_post_detail, timeout=60*15)
            return render_post_detail

    else:
        return JsonResponse({'error': 'You\'ve tried bad access'})


def post_list(request, page, lang):
    if request.method == "GET":
        cache_post_list = cache.get('post_list'+lang+page)
        if cache_post_list is not None:
            return cache_post_list
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
                posts = post_paginator.page(page)
            except PageNotAnInteger:
                posts = post_paginator.page(1)
            except EmptyPage:
                posts = post_paginator.page(post_paginator.num_pages)

            template = switch_post_list_template_by_lang(lang)

            render_post_list = render(request, template, {'posts': posts, 'lang': lang})

            cache.set('post_list'+lang+page, render_post_list, timeout=60*15)
            return render_post_list

    else:
        return JsonResponse({'error': 'You\'ve tried bad access'})
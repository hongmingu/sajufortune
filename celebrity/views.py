from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.shortcuts import redirect, render
from django.template import RequestContext
from django.http import Http404

from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.mail import EmailMessage
import re
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model
from django.conf import settings
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.db import IntegrityError
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.utils.timezone import now, timedelta
import json
import urllib
from urllib.parse import urlparse
import ssl
from bs4 import BeautifulSoup
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404

from post.models import Post
from post.models import PostEnglish

from dayemotion.models import DayEmotion
from daylove.models import DayLove
from daymoney.models import DayMoney
from dayrelationships.models import DayRelationships
from dayoverall.models import DayOverall
from daywork.models import DayWork
from website.utils import *
from django.core.cache import cache
from django.db.models import Q
from django.db.models.functions import Lower
from celebrity.utils import *
# Create your views here.


def celeb_profile(request, lang, num):
    if request.method == "GET":
        cache_celeb_profile = cache.get('celeb_profile'+lang+num)
        if cache_celeb_profile is not None:
            return cache_celeb_profile
        else:
            cache_celebrity_objects_get = cache.get('celebrity_objects_get'+num)
            if cache_celebrity_objects_get is not None:
                celeb = cache_celebrity_objects_get
            else:
                try:
                    celeb = Celebrity.objects.get(pk=num)
                except Celebrity.DoesNotExist:
                    return render(request, '404.html', )
                cache.set('celebrity_objects_get'+num, celeb, timeout=None)

            cache_post_objects_filter = cache.get('post_objects_filter'+num)
            if cache_post_objects_filter is not None:
                posts = cache_post_objects_filter
            else:
                posts = Post.objects.filter(celebrity=celeb)
                cache.set('post_objects_filter'+num, posts, timeout=None)

            template = switch_profile_celeb_template_by_lang(lang)

            render_celeb_profile = render(request, template, {'lang': lang,
                                              'celeb': celeb,
                                              'posts': posts, })

            cache.set('celeb_profile' + lang + num, render_celeb_profile, timeout=None)

            return render_celeb_profile
    else:
        JsonResponse({"NONO": "Don't do that"})


def celeb_list_text(request, lang):
    if request.method == "GET":
        cache_celeb_list_text = cache.get('celeb_list_text'+lang)
        if cache_celeb_list_text is not None:
            return cache_celeb_list_text
        else:
            cache_celebrity_objects_all_lower = cache.get('celebrity_objects_all_lower')
            if cache_celebrity_objects_all_lower is not None:
                celebs = cache_celebrity_objects_all_lower
            else:
                celebs = Celebrity.objects.all().order_by(Lower('celebrityenglish__name'))
                cache.set('celebrity_objects_all_lower', celebs, timeout=None)
        template = switch_celeb_text_list_template_by_lang(lang)
        render_celeb_list_text = render(request, template, {'celebs': celebs, 'lang': lang})
        cache.set('celeb_list_text'+lang, render_celeb_list_text, timeout=None)
        return render_celeb_list_text
    else:
        return JsonResponse({'error': 'You\'ve tried bad access'})


def celeb_list(request, lang, page):
    if request.method == "GET":
        cache_celeb_list = cache.get('celeb_list'+lang+page)
        if cache_celeb_list is not None:
            return cache_celeb_list
        else:
            cache_celeb_objects_all = cache.get('celebrity_objects_all')
            if cache_celeb_objects_all is not None:
                celeb_all = cache_celeb_objects_all
            else:
                celeb_all = Celebrity.objects.all()

            celeb_paginator = Paginator(celeb_all, 10)

            try:
                celebs = celeb_paginator.page(page)
            except PageNotAnInteger:
                celebs = celeb_paginator.page(1)
            except EmptyPage:
                celebs = celeb_paginator.page(celeb_paginator.num_pages)

            template = switch_celeb_list_template_by_lang(lang)
            render_celeb_list = render(request, template, {'celebs': celebs, 'lang': lang})
            cache.set('celeb_list'+lang+page, render_celeb_list, timeout=None)
            return render_celeb_list

    else:
        return JsonResponse({'error': 'You\'ve tried bad access'})


def celeb_day(request, lang, num):
    if request.method == "GET":

        try:
            celeb = Celebrity.objects.get(pk=num)
        except Celebrity.DoesNotExist:
            return render(request, 'post/not_exist_post_default.html', {'lang': lang})

        birthday_year_raw = celeb.birthday_year
        birthday_month_raw = celeb.birthday_month
        birthday_day_raw = celeb.birthday_day
        target_year_raw = request.GET.get('ty', None)
        target_month_raw = request.GET.get('tm', None)
        target_day_raw = request.GET.get('td', None)

        cache_celeb_day = cache.get('celeb_day' + lang +
                              birthday_year_raw + birthday_month_raw + birthday_day_raw +
                              target_year_raw + target_month_raw + target_day_raw )

        if cache_celeb_day is not None:
            return cache_celeb_day
        else:
            if birthday_year_raw is None or birthday_month_raw is None or birthday_day_raw is None \
                    or target_year_raw is None or target_month_raw is None or target_day_raw is None:
                # 제공되지 않은 값이 있을 경우
                return render(request, '404.html', )

            try:
                birthday_year = int(birthday_year_raw)
                birthday_month = int(birthday_month_raw)
                birthday_day = int(birthday_day_raw)
                target_year = int(target_year_raw, 16)
                target_month = int(target_month_raw, 16)
                target_day = int(target_day_raw, 16)
            except ValueError:
                # 값이 제대로 변형되지 않은 경우
                return render(request, '404.html')

            if not validate_date(birthday_year, birthday_month, birthday_day, target_year, target_month, target_day):
                # 값이 변형되었더라도 제대로 된 기간을 제시하지 않은 경우
                return render(request, '404.html')

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

            for i in cache_list:
                if cache_list[i] is None:
                    try:
                        result = get_day_fortune_model_by_index(i).objects.get(pk=num_list[i])
                    except get_day_fortune_model_by_index(i).DoesNotExist:
                        return render(request, '404.html',)
                    cache.set('day' + str(i) + ':' + num_list[i], result, timeout=None)
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

            # post 에서 랜덤으로 배정해주거나, 다른 유명인의 투데이도 보라고 해주기 => 유명인 프로필 데이터랑 타겟데이 나눠야함.
            cache_celebrity_objects_all_exclude = cache.get('celebrity_objects_all_exclude'+celeb.pk)
            if cache_celebrity_objects_all_exclude is not None:
                celeb_list = cache_celebrity_objects_all_exclude.order_by('?')
            else:
                celeb_queryset_exclude = Celebrity.objects.all().exclude(pk=celeb.pk)
                cache.set('celebrity_objects_all_exclude'+celeb.pk, celeb_queryset_exclude, timeout=None)
                celeb_list = celeb_queryset_exclude.order_by('?')

            celeb_paginator = Paginator(celeb_list, 2)
            try:
                other_celebs = celeb_paginator.page(1)
            except EmptyPage:
                other_celebs = celeb_paginator.page(celeb_paginator.num_pages)

            template = switch_celeb_day_template_by_lang(lang)
            render_celeb_day = render(request, template, {'lang': lang,
                                              'birthday': birthday_dict,
                                              'target': target_dict,
                                              'celeb': celeb,
                                              'other_celebs': other_celebs,
                                              'overall': cache_list[0],
                                                'emotion': cache_list[1],
                                                'love': cache_list[2],
                                                'money': cache_list[3],
                                                'relationships': cache_list[4],
                                                'work': cache_list[5], })
            cache.set('celeb_day' + lang +
                              birthday_year_raw + birthday_month_raw + birthday_day_raw +
                              target_year_raw + target_month_raw + target_day_raw, render_celeb_day, timeout=60*10)
            return render_celeb_day
    else:
        return JsonResponse({'Hello': 'You\'ve got wrong access! may god bless you.'})


# /* 셀럽 리스트 페이지, 셀럽 디테일 페이지(셀럽 디테일 페이지에 포스트 목록이랑 셀럽의 투데이, 투모로우, 등등 보기 버튼 필요), 포스트 페이지에 셀럽 프로필로 가기 버튼 필요,
# 개인 결과 페이지에 셀럽의 오늘이나 셀럽의 내일은 어떨까요 알아보는 버튼 추가 유기적으로 돌아가게 */

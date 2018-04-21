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
from post.utils import *
from website.utils import *

from dayemotion.models import DayEmotion
from daylove.models import DayLove
from daymoney.models import DayMoney
from dayrelationships.models import DayRelationships
from dayoverall.models import DayOverall
from daywork.models import DayWork

from django.core.cache import cache

# Create your views here.


def post_detail(request, num, lang):
    if request.method == "GET":
        try:
            post = Post.objects.get(pk=num)
        except Post.DoesNotExist:
            return render(request, '404.html', )
        birthday_year_raw = post.celebrity.birthday_year
        birthday_month_raw = post.celebrity.birthday_month
        birthday_day_raw = post.celebrity.birthday_day
        target_year_raw = post.target_year
        target_month_raw = post.target_month
        target_day_raw = post.target_day

        cache_post_detail = cache.get('post_detail' + lang +
                              birthday_year_raw + birthday_month_raw + birthday_day_raw +
                              target_year_raw + target_month_raw + target_day_raw)
        if cache_post_detail is not None:
            return cache_post_detail
        else:
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

            cache_post_queryset = cache.get('post_objects_all')

            if cache_post_queryset is not None:
                post_queryset = cache_post_queryset
            else:
                post_queryset = Post.objects.all()
                cache.set('post_objects_all', post_queryset, timeout=None)

            post_all = post_queryset.exclude(pk=num).order_by('?')
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
            cache.set('post_detail' + lang +
                              birthday_year_raw + birthday_month_raw + birthday_day_raw +
                              target_year_raw + target_month_raw + target_day_raw, render_post_detail, timeout=60*10)
            return render_post_detail

    else:
        return JsonResponse({'error': 'You\'ve tried bad access'})


def post_list(request, page, lang):
    if request.method == "GET":
        page = request.GET.get(page, 1)
        post_all = Post.objects.all().order_by('-created')
        post_paginator = Paginator(post_all, 10)

        try:
            posts = post_paginator.page(page)
        except PageNotAnInteger:
            posts = post_paginator.page(1)
        except EmptyPage:
            posts = post_paginator.page(post_paginator.num_pages)

        template = switch_post_list_template_by_lang(lang)

        return render(request, template, {'posts': posts, 'lang': lang})

    else:
        return JsonResponse({'error': 'You\'ve tried bad access'})
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

# Create your views here.


def profile_celeb(request, lang, num):
    if request.method == "GET":
        celeb = None
        try:
            celeb = Celebrity.objects.get(pk=num)
        except Celebrity.DoesNotExist:
            return render(request, 'post/not_exist_post_default.html', )

        posts = None
        posts = Post.objects.filter(celebrity=celeb)
        other_celebs = None
        other_celebs = Celebrity.objects.all().exclude(pk=num)

        return render(request, 'celebrity/profile/celeb_profile_eng.html', {'lang': lang,
                                                                    'celeb': celeb,
                                                                    'other_celeb': other_celebs,
                                                                    'posts': posts, })
    else:
        JsonResponse({"NONO": "Don't do that"})


def switch_get_celeb_list_template(lang):
    return {
        'ara': 'post/detail_ara.html',
        'chi': 'post/detail_chi.html',
        'eng': 'post/detail_eng.html',
        'por': 'post/detail_por.html',
        'spa': 'post/detail_spa.html',
    }.get(lang, 'eng')


def list_text_celeb(request, lang):
    if request.method == "GET":
        celebs = Celebrity.objects.all().order_by(Lower('celebrityenglish__name'))
        return render(request, 'celebrity/list/celeb_text_list_eng.html', {'celebs': celebs,
                                                                      'lang': lang})
    else:
        return JsonResponse({'error': 'You\'ve tried bad access'})


def list_celeb(request, lang, page):
    if request.method == "GET":

        celeb_all = Celebrity.objects.all()
        celeb_paginator = Paginator(celeb_all, 10)

        try:
            celebs = celeb_paginator.page(page)
        except PageNotAnInteger:
            celebs = celeb_paginator.page(1)
        except EmptyPage:
            celebs = celeb_paginator.page(celeb_paginator.num_pages)

        return render(request, 'celebrity/list/celeb_list_eng.html', {'celebs': celebs, 'lang': lang})

    else:
        return JsonResponse({'error': 'You\'ve tried bad access'})


def day_celeb(request, lang, num):
    if request.method == "GET":
        try:
            celeb = Celebrity.objects.get(pk=num)
        except Celebrity.DoesNotExist:
            return render(request, 'post/not_exist_post_default.html',)
        birthday_year = celeb.birthday_year
        birthday_month = celeb.birthday_month
        birthday_day = celeb.birthday_day
        target_year = request.GET.get('ty', None)
        target_month = request.GET.get('tm', None)
        target_day = request.GET.get('td', None)
        if birthday_year is None or birthday_month is None or birthday_day is None \
                or target_year is None or target_month is None or target_day is None:
            # 제공되지 않은 값이 있을 경우
            return render(request, 'celebrity/day/celeb_day_eng.html', )

        try:
            birthday_year = int(birthday_year)
            birthday_month = int(birthday_month)
            birthday_day = int(birthday_day)
            target_year = int(target_year, 16)
            target_month = int(target_month, 16)
            target_day = int(target_day, 16)
        except ValueError:
            # 값이 제대로 변형되지 않은 경우
            return render(request, 'celebrity/day/celeb_day_eng.html', )

        if not validate_date(birthday_year, birthday_month, birthday_day, target_year, target_month, target_day):
            # 값이 변형되었더라도 제대로 된 기간을 제시하지 않은 경우
            return render(request, 'celebrity/day/celeb_day_eng.html', )

        result_num = get_result_num(birthday_year, birthday_month, birthday_day, target_year, target_month, target_day)

        overall_num = get_overall_num(result_num)
        emotion_num = get_emotion_num(result_num)
        love_num = get_love_num(result_num)
        money_num = get_money_num(result_num)
        relationship_num = get_relationship_num(result_num)
        work_num = get_work_num(result_num)

        try:
            overall = DayOverall.objects.get(pk=1)
            emotion = DayEmotion.objects.get(pk=1)
            love = DayLove.objects.get(pk=1)
            money = DayMoney.objects.get(pk=1)
            relationships = DayRelationships.objects.get(pk=1)
            work = DayWork.objects.get(pk=1)
        except ObjectDoesNotExist:
            # 여러가지 계산에 에러가 난 경우
            # 이 경우들에 되돌아가기를 만들어줘야 함.
            return render(request, 'post/not_exist_post_default.html', )

        birthday_dict = dict()
        target_dict = dict()
        birthday_dict['year'] = birthday_year
        birthday_dict['month'] = birthday_month
        birthday_dict['day'] = birthday_day
        target_dict['year'] = target_year
        target_dict['month'] = target_month
        target_dict['day'] = target_day

        # post 에서 랜덤으로 배정해주거나, 다른 유명인의 투데이도 보라고 해주기 => 유명인 프로필 데이터랑 타겟데이 나눠야함.

        celeb_list = Celebrity.objects.all().exclude(pk=celeb.pk).order_by('?')
        celeb_paginator = Paginator(celeb_list, 2)
        try:
            other_celebs = celeb_paginator.page(1)
        except EmptyPage:
            other_celebs = celeb_paginator.page(celeb_paginator.num_pages)

        return render(request, 'celebrity/day/celeb_day_eng.html', {'lang': lang,
                                                                'birthday': birthday_dict,
                                                                'target': target_dict,
                                                                'celeb': celeb,
                                                                'other_celebs': other_celebs,
                                                                'overall': overall,
                                                                    'emotion': emotion,
                                                                    'love': love,
                                                                    'money': money,
                                                                    'relationships': relationships,
                                                                    'work': work, })
    else:
        return JsonResponse({'Hello': 'You\'ve got wrong access! may god bless you.'})

def list_default(request, page):
    if request.method == "POST":
        return JsonResponse({'error': 'You\'ve tried bad access'})
    else:
        page = request.GET.get(page, 1)
        post_all = Post.objects.all()
        post_paginator = Paginator(post_all, 10)

        try:
            posts = post_paginator.page(page)
        except PageNotAnInteger:
            posts = post_paginator.page(1)
        except EmptyPage:
            posts = post_paginator.page(post_paginator.num_pages)
        return render(request, 'post/list_default.html', {'posts': posts})


def switch_get_post_detail_template(lang):
    return {
        'ara': 'post/detail_ara.html',
        'chi': 'post/detail_chi.html',
        'eng': 'post/detail_eng.html',
        'por': 'post/detail_por.html',
        'spa': 'post/detail_spa.html',
    }.get(lang, 'eng')


def detail(request, num, lang):
    if request.method == "GET":
        try:
            post = Post.objects.get(pk=num)
        except Post.DoesNotExist:
            return render(request, 'post/not_exist_post_default.html', )

        int_num = int(num)
        # to get next two pages

        birthday_year = post.celebrity.birthday_year
        birthday_month = post.celebrity.birthday_month
        birthday_day = post.celebrity.birthday_day
        target_year = post.target_year
        target_month = post.target_month
        target_day = post.target_day

        result_num = int(((birthday_year + target_day) * 1) + ((birthday_month + target_month) * 3) +
                         ((birthday_day + target_year) * 5))

        overall_num = (result_num % 106) + 1
        emotion_num = (result_num % 105) + 1
        love_num = (result_num % 104) + 1
        money_num = (result_num % 103) + 1
        relationship_num = (result_num % 102) + 1
        work_num = (result_num % 101) + 1

        try:
            overall = DayOverall.objects.get(pk=1)
            emotion = DayEmotion.objects.get(pk=1)
            love = DayLove.objects.get(pk=1)
            money = DayMoney.objects.get(pk=1)
            relationships = DayRelationships.objects.get(pk=1)
            work = DayWork.objects.get(pk=1)
        except ObjectDoesNotExist:
            return render(request, 'post/not_exist_post_default.html', )

        template = switch_get_post_detail_template(lang)

        post_option_1 = None
        try:
            post_option_1 = Post.objects.get(pk=int_num - 3)
        except Post.DoesNotExist:
            post_option_2 = None

        post_option_2 = None
        try:
            post_option_2 = Post.objects.get(pk=int_num - 5)
        except Post.DoesNotExist:
            post_option_2 = None

        return render(request, template, {'post': post,
                                          'post_option_1': post_option_1,
                                          'post_option_2': post_option_2,
                                          'lang': lang,
                                          'overall': overall,
                                          'emotion': emotion,
                                          'love': love,
                                          'money': money,
                                          'relationships': relationships,
                                          'work': work, })

    else:
        return JsonResponse({'error': 'You\'ve tried bad access'})


def post_list(request, page, lang):
    if request.method == "GET":
        page = request.GET.get(page, 1)
        post_all = Post.objects.all()
        post_paginator = Paginator(post_all, 10)

        try:
            posts = post_paginator.page(page)
        except PageNotAnInteger:
            posts = post_paginator.page(1)
        except EmptyPage:
            posts = post_paginator.page(post_paginator.num_pages)

        if lang == 'ara':
            return render(request, 'post/list/list_ara.html', {'posts': posts, 'lang': lang})
        elif lang == 'chi':
            return render(request, 'post/list/list_chi.html', {'posts': posts, 'lang': lang})
        elif lang == 'eng':
            return render(request, 'post/list/list_eng.html', {'posts': posts, 'lang': lang})
        elif lang == 'por':
            return render(request, 'post/list/list_por.html', {'posts': posts, 'lang': lang})
        elif lang == 'spa':
            return render(request, 'post/list/list_spa.html', {'posts': posts, 'lang': lang})

    else:
        return JsonResponse({'error': 'You\'ve tried bad access'})


def post_detail(request, ftype, num, lang):
    if request.method == "POST":
        return JsonResponse({'error': 'You\'ve tried bad access'})
    else:
        post = Post.objects.get_object_or_404(pk=num)

        if lang == 'ara':
            if ftype == 'overall':
                return render(request, 'post/overall_ara.html', {'post': post})
            elif ftype == 'detail':
                return render(request, 'post/detail/detail_ara.html', {'post': post})
        elif lang == 'chi':
            if ftype == 'overall':
                return render(request, 'post/overall_chi.html', {'post': post})
            elif ftype == 'detail':
                return render(request, 'post/detail_chi.html', {'post': post})
        elif lang == 'eng':
            if ftype == 'overall':
                return render(request, 'post/overall_eng.html', {'post': post})
            elif ftype == 'detail':
                return render(request, 'post/detail/detail_eng.html', {'post': post})
        elif lang == 'por':
            if ftype == 'overall':
                return render(request, 'post/overall_por.html', {'post': post})
            elif ftype == 'detail':
                return render(request, 'post/detail_por.html', {'post': post})
        elif lang == 'spa':
            if ftype == 'overall':
                return render(request, 'post/overall_spa.html', {'post': post})
            elif ftype == 'detail':
                return render(request, 'post/detail_spa.html', {'post': post})

# /* 셀럽 리스트 페이지, 셀럽 디테일 페이지(셀럽 디테일 페이지에 포스트 목록이랑 셀럽의 투데이, 투모로우, 등등 보기 버튼 필요), 포스트 페이지에 셀럽 프로필로 가기 버튼 필요,
# 개인 결과 페이지에 셀럽의 오늘이나 셀럽의 내일은 어떨까요 알아보는 버튼 추가 유기적으로 돌아가게 */

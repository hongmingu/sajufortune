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

from dayemotion.models import DayEmotion
from daylove.models import DayLove
from daymoney.models import DayMoney
from dayrelationships.models import DayRelationships
from dayoverall.models import DayOverall
from daywork.models import DayWork

from django.core.cache import cache

# Create your views here.


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
            return render(request, 'post/list_ara.html', {'posts': posts, 'lang': lang})
        elif lang == 'chi':
            return render(request, 'post/list_chi.html', {'posts': posts, 'lang': lang})
        elif lang == 'eng':
            return render(request, 'post/list_eng.html', {'posts': posts, 'lang': lang})
        elif lang == 'por':
            return render(request, 'post/list_por.html', {'posts': posts, 'lang': lang})
        elif lang == 'spa':
            return render(request, 'post/list_spa.html', {'posts': posts, 'lang': lang})

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
                return render(request, 'post/detail_ara.html', {'post': post})
        elif lang == 'chi':
            if ftype == 'overall':
                return render(request, 'post/overall_chi.html', {'post': post})
            elif ftype == 'detail':
                return render(request, 'post/detail_chi.html', {'post': post})
        elif lang == 'eng':
            if ftype == 'overall':
                return render(request, 'post/overall_eng.html', {'post': post})
            elif ftype == 'detail':
                return render(request, 'post/detail_eng.html', {'post': post})
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

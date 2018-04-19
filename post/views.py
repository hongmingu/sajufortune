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
            return render(request, 'post/not_exist_post_default.html', )

        int_num = int(num)
        # to get next two pages

        birthday_year = int(post.celebrity.birthday_year)
        birthday_month = int(post.celebrity.birthday_month)
        birthday_day = int(post.celebrity.birthday_day)
        target_year = int(post.target_year)
        target_month = int(post.target_month)
        target_day = int(post.target_day)

        if birthday_year is None or birthday_month is None or birthday_day is None \
                or target_year is None or target_month is None or target_day is None:
            # 제공되지 않은 값이 있을 경우
            return render(request, 'celebrity/day/celeb_day_eng.html', {'lang': lang})

        if not validate_date(birthday_year, birthday_month, birthday_day, target_year, target_month, target_day):
            # 값이 변형되었더라도 제대로 된 기간을 제시하지 않은 경우
            return render(request, 'celebrity/day/celeb_day_eng.html', {'lang': lang})

        result_num = int(((birthday_year + target_day) * 1) + ((birthday_month + target_month) * 3) +
                         ((birthday_day + target_year) * 5))

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
            return render(request, 'post/not_exist_post_default.html', )

        post_all = Post.objects.all().exclude(pk=num).order_by('?')
        post_paginator = Paginator(post_all, 2)

        other_posts = post_paginator.page(1)

        birthday_dict = dict()
        target_dict = dict()
        birthday_dict['year'] = birthday_year
        birthday_dict['month'] = birthday_month
        birthday_dict['day'] = birthday_day
        target_dict['year'] = target_year
        target_dict['month'] = target_month
        target_dict['day'] = target_day

        template = switch_post_detail_template_by_lang(lang)

        return render(request, template, {'post': post,
                                          'other_posts': other_posts,
                                          'lang': lang,
                                          'birthday': birthday_dict,
                                          'target': target_dict,
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
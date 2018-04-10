from website.utils import *
from django.urls import reverse
from django.shortcuts import redirect, render

from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from post.models import Post
from dayemotion.models import DayEmotion
from daylove.models import DayLove
from daymoney.models import DayMoney
from dayoverall.models import DayOverall
from daywork.models import DayWork
from dayrelationships.models import DayRelationships
from django.core.cache import cache


def test(request):
    if request.method == "POST":
        pass
    else:
        get_data = request.GET.get('q', 'default_value')
        get_cache = cache.get_or_set('posts'+get_data, get_data)

        answer = {'q': get_data}
        return render(request, 'website/test.html', {'answer': answer})


def day(request, lang):
    if request.method == "GET":

        birthday_year = request.GET.get('by', None)
        birthday_month = request.GET.get('bm', None)
        birthday_day = request.GET.get('bd', None)
        target_year = request.GET.get('ty', None)
        target_month = request.GET.get('tm', None)
        target_day = request.GET.get('td', None)
        if birthday_year is None or birthday_month is None or birthday_day is None \
                or target_year is None or target_month is None or target_day is None:
            # 제공되지 않은 값이 있을 경우
            return render(request, 'website/day_eng.html', )

        try:
            birthday_year = int(birthday_year, 16)
            birthday_month = int(birthday_month, 16)
            birthday_day = int(birthday_day, 16)
            target_year = int(target_year, 16)
            target_month = int(target_month, 16)
            target_day = int(target_day, 16)
        except ValueError:
            # 값이 제대로 변형되지 않은 경우
            return render(request, 'website/day_eng.html', )

        if not validate_date(birthday_year, birthday_month, birthday_day, target_year, target_month, target_day):
            # 값이 변형되었더라도 제대로 된 기간을 제시하지 않은 경우
            return render(request, 'website/day_eng.html', )

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

        # post에서 랜덤으로 배정해주거나, 다른 유명인의 투데이도 보라고 해주기 => 유명인 프로필 데이터랑 타겟데이 나눠야함.
        post_list = Post.objects.all()
        post_paginator = Paginator(post_list, 10)
        try:
            posts = post_paginator.page(1)
        except PageNotAnInteger:
            posts = post_paginator.page(1)
        except EmptyPage:
            posts = post_paginator.page(post_paginator.num_pages)

        return render(request, 'website/day_eng.html', {'lang': lang,
                                                        'birthday': birthday_dict,
                                                        'target': target_dict,
                                                        'overall': overall,
                                                        'emotion': emotion,
                                                        'love': love,
                                                        'money': money,
                                                        'relationships': relationships,
                                                        'work': work, })
    else:
        return JsonResponse({'Hello': 'You\'ve got wrong access! may god bless you.'})


def main(request):
    if request.method == "GET":

        post_list = Post.objects.all()
        post_paginator = Paginator(post_list, 10)
        try:
            posts = post_paginator.page(1)
        except PageNotAnInteger:
            posts = post_paginator.page(1)
        except EmptyPage:
            posts = post_paginator.page(post_paginator.num_pages)

            # post_paginator.num_pages 는 마지막 페이지를 의미 1페이지가 마지막 페이지면 그렇게 되는거고
        return render(request, 'website/main.html', {'posts': posts,})
    else:
        return JsonResponse({'Hello': 'You\'ve got wrong access! may god bless you.'})


def switch_main_template_by_lang(lang):
    return {
        'ara': 'website/main_ara.html',
        'chi': 'website/main_chi.html',
        'eng': 'website/main_eng.html',
        'por': 'website/main_por.html',
        'spa': 'website/main_ara.html',
    }


def main_lang(request, lang):
    if request.method == "GET":

        if lang == 'eng':
            return redirect(reverse('website:main'))

        post_list = Post.objects.all()
        post_paginator = Paginator(post_list, 10)
        try:
            posts = post_paginator.page(1)
        except PageNotAnInteger:
            posts = post_paginator.page(1)
        except EmptyPage:
            posts = post_paginator.page(post_paginator.num_pages)

        template = switch_main_template_by_lang(lang)
            # post_paginator.num_pages 는 마지막 페이지를 의미 1페이지가 마지막 페이지면 그렇게 되는거고

        return render(request, template, {'posts': posts, 'lang': lang})
    else:
        return JsonResponse({'Hello': 'You\'ve got wrong access! may god bless you.'})


'''

def switch(x):
    return {
        'ara': PostArabic,
        'chi': PostChinese,
        'eng': PostEnglish,
        'por': PostPortuguese,
        'spa': PostSpanish,
    }.get(x, PostAll)
'''


def switch(lang):
    return {
        'ara': 'website/list_ara.html',
        'chi': 'website/list_chi.html',
        'eng': 'website/list_eng.html',
        'por': 'website/list_por.html',
        'spa': 'website/list_spa.html',
    }



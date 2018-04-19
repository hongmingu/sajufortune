from django.shortcuts import render


def get_result_num(birthday_year, birthday_month, birthday_day, target_year, target_month, target_day):
    return int(((birthday_year + target_day) * 1) +
               ((birthday_month + target_month) * 3) +
               ((birthday_day + target_year) * 5))


def get_overall_num(num):
    return (num % 106) + 1


def get_relationship_num(num):
    return (num % 105) + 1


def get_emotion_num(num):
    return (num % 104) + 1


def get_love_num(num):
    return (num % 103) + 1


def get_money_num(num):
    return (num % 102) + 1


def get_work_num(num):
    return (num % 101) + 1


def validate_date(birthday_year, birthday_month, birthday_day, target_year, target_month, target_day):
    if 1800 <= birthday_year \
            and 1800 <= target_year \
            and (1 <= (birthday_month and target_month) <= 12) \
            and (1 <= (birthday_day and target_day) <= 31):
        # 값이 변형되었더라도 제대로 된 기간을 제시하지 않은 경우
        return True
    else:
        return False


def switch_day_template_by_lang(lang):
    return {
        'ara': 'website/day/day_ara.html',
        'chi': 'website/day/day_chi.html',
        'eng': 'website/day/day_eng.html',
        'por': 'website/day/day_por.html',
        'spa': 'website/day/day_spa.html',
    }.get(lang, 'website/day/day_eng.html')


def switch_main_lang_template_by_lang(lang):
    return {
        'ara': 'website/main/main_ara.html',
        'chi': 'website/main/main_chi.html',
        'eng': 'website/main/main_eng.html',
        'por': 'website/main/main_por.html',
        'spa': 'website/main/main_spa.html',
    }.get(lang, 'website/main/main_eng.html')


def switch_about_template_by_lang(lang):
    return {
        'ara': 'website/about/about_ara.html',
        'chi': 'website/about/about_chi.html',
        'eng': 'website/about/about_eng.html',
        'por': 'website/about/about_por.html',
        'spa': 'website/about/about_spa.html',
    }.get(lang, 'website/about/about_eng.html')


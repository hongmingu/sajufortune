
def switch_profile_celeb_template_by_lang(lang):
    return {
        'ara': 'celebrity/profile/celeb_profile_ara.html',
        'chi': 'celebrity/profile/celeb_profile_chi.html',
        'eng': 'celebrity/profile/celeb_profile_eng.html',
        'por': 'celebrity/profile/celeb_profile_por.html',
        'spa': 'celebrity/profile/celeb_profile_spa.html',
    }.get(lang, 'celebrity/profile/celeb_profile_spa.html')


def switch_celeb_text_list_template_by_lang(lang):
    return {
        'ara': 'celebrity/list/celeb_text_list_ara.html',
        'chi': 'celebrity/list/celeb_text_list_chi.html',
        'eng': 'celebrity/list/celeb_text_list_eng.html',
        'por': 'celebrity/list/celeb_text_list_por.html',
        'spa': 'celebrity/list/celeb_text_list_spa.html',
    }.get(lang, 'celebrity/list/celeb_text_list_spa.html')


def switch_celeb_list_template_by_lang(lang):
    return {
        'ara': 'celebrity/list/celeb_list_ara.html',
        'chi': 'celebrity/list/celeb_list_chi.html',
        'eng': 'celebrity/list/celeb_list_eng.html',
        'por': 'celebrity/list/celeb_list_por.html',
        'spa': 'celebrity/list/celeb_list_spa.html',
    }.get(lang, 'celebrity/list/celeb_list_eng.html')


def switch_celeb_day_template_by_lang(lang):
    return {
        'ara': 'celebrity/day/celeb_day_ara.html',
        'chi': 'celebrity/day/celeb_day_chi.html',
        'eng': 'celebrity/day/celeb_day_eng.html',
        'por': 'celebrity/day/celeb_day_por.html',
        'spa': 'celebrity/day/celeb_day_spa.html',
    }.get(lang, 'celebrity/day/celeb_day_eng.html')

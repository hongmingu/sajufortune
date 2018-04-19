from uuid import uuid4


def switch_post_detail_template_by_lang(lang):
    return {
        'ara': 'post/detail/detail_ara.html',
        'chi': 'post/detail/detail_chi.html',
        'eng': 'post/detail/detail_eng.html',
        'por': 'post/detail/detail_por.html',
        'spa': 'post/detail/detail_spa.html',
    }.get(lang, 'post/detail/detail_eng.html')


def switch_post_list_template_by_lang(lang):
    return {
        'ara': 'post/list/list_ara.html',
        'chi': 'post/list/list_chi.html',
        'eng': 'post/list/list_eng.html',
        'por': 'post/list/list_por.html',
        'spa': 'post/list/list_spa.html',
    }.get(lang, 'post/list/list_eng.html')

'''
def get_picture_url(self, filename):
    # I like to change the filename, but feel free to don't do it
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid4().hex, ext)

    return "images/products/%(category_id)s/%(product_slug)s/%(file_name)s" % {
        'category_id': instance.product.category.id,
        'product_slug': instance.product.slug,
        'filename': filename,
    }
'''
from .base import *
import json

SETTINGS_DIR = os.path.join('/django_settings', 'debug')
SETTINGS_FILE = os.path.join(SETTINGS_DIR, 'debug.json')

with open(SETTINGS_FILE) as f:
    settings_json = json.loads(f.read())

DEBUG = False

SECRET_KEY = settings_json['django']['secret_key']
ALLOWED_HOSTS = settings_json['django']['allowed_hosts']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'dayoverall',
    'daywork',
    'daylove',
    'daymoney',
    'dayemotion',
    'dayrelationships',
    'post',
    'celebrity',
    'website',
    'debug_toolbar',
]

# django-debug-toolbar
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # this is for debug-toolbar
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# this is for debug-toolbar
INTERNAL_IPS = ('127.0.0.1',)

# caches
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# WSGI application
WSGI_APPLICATION = 'sajufortune.wsgi.local.application'

# Static settings
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'collectedstatic')
# 이 폴더가 없으면 만들어질 것이다.
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
# 각 media 파일에 대한 URL Prefix
MEDIA_URL = '/media/'
# 항상 / 로 끝나도록 설정
# MEDIA_URL = 'http://static.myservice.com/media/' 다른 서버로 media 파일 복사시
# 업로드된 파일을 저장할 디렉토리 경로
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_dir')
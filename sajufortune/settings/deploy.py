from .base import *
import json

SETTINGS_DIR = os.path.join('/django_settings', 'deploy')
SETTINGS_FILE = os.path.join(SETTINGS_DIR, 'deploy.json')

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
    'django.contrib.sites',
    'django.contrib.sitemaps',
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
]

SITE_ID = 1
# django-debug-toolbar
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

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
WSGI_APPLICATION = 'sajufortune.wsgi.deploy.application'

# Static settings
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = 'AKIAJTAXI3XLOAQCOXPA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'sajufortune-s3'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=259200',
}

AWS_S3_CUSTOM_DOMAIN = 'd3m4mlntjbzekh.cloudfront.net'

# Static Setting
STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN

# Media Setting
MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN

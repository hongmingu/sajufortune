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
        "LOCATION": settings_json['redis']['default']['location'],
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# database
DATABASES = {
    'default': {
        'ENGINE': settings_json['database']['default']['engine'],
        'NAME': settings_json['database']['default']['name'],
        'USER': settings_json['database']['default']['user'],
        'PASSWORD': settings_json['database']['default']['password'],
        'HOST': settings_json['database']['default']['host'],
        'PORT': settings_json['database']['default']['port'],
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}

# WSGI application
WSGI_APPLICATION = 'sajufortune.wsgi.deploy.application'

# Static settings
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = settings_json['cdn']['aws']['aws_access_key_id']
AWS_SECRET_ACCESS_KEY = settings_json['cdn']['aws']['aws_secret_access_key']
AWS_STORAGE_BUCKET_NAME = settings_json['cdn']['aws']['aws_storage_bucket_name']
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=259200',
}

AWS_S3_CUSTOM_DOMAIN = 'd3m4mlntjbzekh.cloudfront.net'

# Static Setting
STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN

# Media Setting
MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN

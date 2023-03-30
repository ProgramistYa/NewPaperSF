"""
Django settings for NewsPaper project.
Generated by 'django-admin startproject' using Django 4.1.6.
"""
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

SITE_ID = 1

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'news.apps.NewsConfig',
    'accounts',
    'sign',
    'protect',
    'fpages',
    'django_filters',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    #включите поставщиков, которых вы хотите включить:
    'allauth.socialaccount.providers.google',
    'django_apscheduler',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'NewsPaper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                #`allauth` нужно это от django
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'NewsPaper.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = [
    # Необходимо войти в систему под именем пользователя в админке Django, независимо от `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # специальные методы аутентификации `allauth`, такие как вход по электронной почте
    'allauth.account.auth_backends.AuthenticationBackend',
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True
#USE_L10N = True
USE_TZ = True


STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

# декоратор перенаправит пользователя на страницу входа. /accounts
LOGIN_URL = '/sign/login/'
LOGIN_REDIRECT_URL = '/'

#Дальнейшая конфигурация проекта будет ориентирована на различные способы регистрации/авторизации.
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'

#Чтобы allauth распознал нашу форму как ту, что должна выполняться вместо формы по умолчанию
ACCOUNT_FORMS = {'signup': 'sign.models.BaseRegisterForm'}

SITE_URL = 'http://127.0.0.1:8000'
#Рассылка с емайла на емаайл
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = 's-ya98'
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = 's-ya98@ya.ru'

#Для админки.
ADMINS = [
    ('prezidentlink', 'Prezidentlink@yandex.ru'),
]
SERVER_EMAIL = 's-ya98@ya.ru'

# формат даты, которую будет воспринимать наш задачник (вспоминаем модуль по фильтрам)
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
# если задача не выполняется за 25 секунд, то она автоматически снимается, можете поставить время побольше, но как правило, это сильно бьёт по производительности сервера
APSCHEDULER_RUN_NOW_TIMEOUT = 25  # Seconds
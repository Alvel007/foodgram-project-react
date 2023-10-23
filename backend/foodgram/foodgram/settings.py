import os
from pathlib import Path

from django.core.management.utils import get_random_secret_key
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', default=get_random_secret_key())

DEBUG = os.getenv('DEBUG', default=False)

ALLOWED_HOSTS = ['127.0.0.1',
                 'localhost',
                 os.getenv('HOST_IP'),
                 os.getenv('HOST_NAME')]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'csvimport.app.CSVImportConf',
    'rest_framework',
    'rest_framework.authtoken',
    'users.apps.UsersConfig',
    'api.apps.ApiConfig',
    'recipes.apps.RecipesConfig',
    'django_filters',
    'djoser',
    'spectrum',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'foodgram.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'foodgram.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'foodgram'),
        'USER': os.getenv('POSTGRES_USER', 'foodgram_user'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'foodgram_password'),
        'HOST': os.getenv('DB_HOST', 'postgre_db_prod'),
        'PORT': os.getenv('DB_PORT', 5432),
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


LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/backend_static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/backend_media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.User'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly'
    ],
    'DEFAULT_PAGINATION_CLASS': 'api.paginations.CustomPagination',
    'PAGE_SIZE': 6,
}

MIN_COOKING_TIME = 1

MIN_INGREDIENT_AMOUNT = 1

NAME_SHOPPING_CART_PDF = 'shopping_cart.pdf'

EMPTY_VALUE_DISPLAY = '-empty-'

PAGINATION_SIZE = 6

DJOSER = {
    'LOGIN_FIELD': 'email',
    'HIDE_USERS': False,
    'SERIALIZERS': {'user': 'users.serializers.UserSerializer',
                    'user_create': 'users.serializers.CreateUserSerializer',
                    'current_user': 'users.serializers.UserSerializer',
                    },
    'PERMISSIONS': {'user': ['rest_framework.permissions.IsAuthenticated'],
                    'user_delete': ['rest_framework.permissions.IsAdminUser'],
                    },
}

COLOR_TAGS = [
    ('#800000', 'Тёмно-бордовый'),
    ('#FF0000', 'Красный'),
    ('#FF6347', 'Томатный'),
    ('#FF4500', 'Оранжево-красный'),
    ('#FFA500', 'Оранжевый'),
    ('#FFD700', 'Золотой'),
    ('#FFFF00', 'Жёлтый'),
    ('#ADFF2F', 'Зелёно-жёлтый'),
    ('#008000', 'Зелёный'),
    ('#00FF00', 'Лаймовый'),
    ('#40E0D0', 'Бирюзовый'),
    ('#00FFFF', 'Морская волна'),
    ('#00008B', 'Тёмно-синий'),
    ('#0000FF', 'Синий'),
    ('#800080', 'Фиолетовый'),
    ('#FF00FF', 'Маджента'),
    ('#DC143C', 'Малиновый'),
    ('#A52A2A', 'Коричневый'),
    ('#808080', 'Серый'),
    ('#000000', 'Чёрный'),
]

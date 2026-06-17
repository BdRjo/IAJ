"""
Django settings for core project.
"""

from pathlib import Path
import os
import dj_database_url # تمت إضافتها للربط بقاعدة بيانات Neon

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# تم تعديلها لتأخذ مفتاح الأمان من السيرفر، أو تستخدم المحلي إذا لم يجده
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-_vr60vi(0iqx)t8i@j9xmoo_#ca24=n1joalaumf4u#10gt%c=')

# SECURITY WARNING: don't run with debug turned on in production!
# تم تعديلها لتكون True محلياً، وتكون False أونلاين
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'award',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # تمت إضافتها لرفع ملفات CSS و JS أونلاين
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'award/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'award.context_processors.ticker_context',               
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# إعداد قاعدة البيانات السحابية Neon (يتم تفعيله فقط إذا وجد الرابط أونلاين)
if os.environ.get('DATABASE_URL'):
    DATABASES['default'] = dj_database_url.parse(os.environ.get('DATABASE_URL'), conn_max_age=600)


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/' # لازم يكون فيه سلاش بالبداية

# 1. هنا بنقول للجانغو وين ملفاتك المحلية (اللي فيها Bootstrap وغيره)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'award/static'), # لو مجلد static داخل award، لو مكانه ثاني عدل المسار
]

# 2. هنا المكان اللي بيتجمع فيه الملفات على السيرفر (غيرنا اسمه لـ staticfiles عشان ما يتعارض)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 

# إعداد التخزين (Static للـ WhiteNoise، Media للـ Cloudinary)
STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage", # الصور تروح سحابة
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage", # نجبره يقرأ CSS الجديد
    },
}


# إعدادات الاتصال بـ Cloudinary
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME', 'dd1ylbi9k'),
    'API_KEY': os.environ.get('CLOUDINARY_API_KEY', '488629293359776'),
    'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET', '6VohO8gyigQX2dF2S9z4uPX5MEA'),
}

MEDIA_URL = '/media/'
# تأكد إنك حذفت MEDIA_ROOT خالص

"""
Django settings for golgoth project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&zb8v3lkuvwlk_kqg0ooz!dxj!7z3ss!c(gg_+yu+z#nom-gp#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'golgoth.urls'

WSGI_APPLICATION = 'golgoth.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
STATIC_ROOT = 'static'
STATIC_URL = '/static/'

# https://github.com/imkevinxu/django-kevin

#
# https://django-secure.readthedocs.org/en/latest/index.html
# 
INSTALLED_APPS += ( 'djangosecure', )
MIDDLEWARE_CLASSES += ( 'djangosecure.middleware.SecurityMiddleware', )
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 10
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_FRAME_DENY = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True

#
# https://github.com/teddziuba/django-sslserver
#
INSTALLED_APPS += ( 'sslserver', )

#
# http://django-debug-toolbar.readthedocs.org
# 
INSTALLED_APPS += ( 'debug_toolbar', )
MIDDLEWARE_CLASSES += ( 'debug_toolbar.middleware.DebugToolbarMiddleware', )
INTERNAL_IPS = ('127.0.0.1')

#
# http://django-authtools.readthedocs.org
#
INSTALLED_APPS += ( 'authtools', )
AUTH_USER_MODEL = 'authtools.User'

#
# https://github.com/django-behave/django-behave
#
INSTALLED_APPS += ( 'django_behave', )
# TEST_RUNNER = 'django_behave.runner.DjangoBehaveTestSuiteRunner'

#
# https://github.com/django-nose/django-nose
# http://nose.readthedocs.org
# 
#
INSTALLED_APPS += ( 'django_nose', )
#TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

#
# https://github.com/nvbn/django-bower
#
INSTALLED_APPS += ( 'djangobower', )
STATICFILES_FINDERS += ( 'djangobower.finders.BowerFinder', )
BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'components')
BOWER_INSTALLED_APPS = (
    'jquery#1.9',
    'bootstrap#3.3',
)

#
# golgoth
#
INSTALLED_APPS += ( 'search', )


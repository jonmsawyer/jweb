"""
Django settings for jweb project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

import sys
MD_DEUX_CONTRIB = os.path.join(BASE_DIR, 'jweb', 'inst', 'django-markdown-deux', 'lib')
MD2_CONTRIB = os.path.join(BASE_DIR, 'jweb', 'inst', 'python-markdown2', 'lib')
if os.path.isdir(MD_DEUX_CONTRIB):
    sys.path.insert(0, MD_DEUX_CONTRIB)
if os.path.isdir(MD2_CONTRIB):
    sys.path.insert(0, MD2_CONTRIB)

import re

try:
    from jweb import dev_settings as extra_settings
except:
    from jweb import prod_settings as extra_settings

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = extra_settings.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = extra_settings.DEBUG

TEMPLATE_DEBUG = DEBUG

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)

ALLOWED_HOSTS = extra_settings.ALLOWED_HOSTS

MY_APPS = (
    'www',
    'blog',
)

APPS_NO_STATIC = (
    'markdown_deux',
)

INSTALLED_APPS = MY_APPS + APPS_NO_STATIC + (
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

ROOT_URLCONF = 'jweb.urls'

WSGI_APPLICATION = 'jweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = extra_settings.DATABASES

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = tuple()
for app in MY_APPS:
    STATICFILES_DIRS += (os.path.join(BASE_DIR, app, 'static'),)


# Markdown Part Deux
#from markdown_deux.conf.settings import MARKDOWN_DEUX_DEFAULT_STYLE

MARKDOWN_DEUX_STYLES = {
    "default": {'extras': {'code-friendly': None}, 'safe_mode': 'escape'},
    #"default": MARKDOWN_DEUX_DEFAULT_STYLE,
    "trusted": {
        "extras": {
            "code-friendly": True,
            "link_patterns": [
                (
                    re.compile(r"recipe\s+#?(\d+)\b", re.I),
                    r"http://code.activestate.com/recipes/\1/",
                ),
            ],
            "pattern_replacements": [
                (
                    re.compile(r'\[gist:(\d+)\]', re.I|re.M|re.S),
                    r'<script src="https://gist.github.com/jonmsawyer/\1.js"></script>',
                ),
            ],
        },
        # Allow raw HTML (WARNING: don't use this for user-generated
        # Markdown for your site!).
        "safe_mode": False,
    },
    # Here is what http://code.activestate.com/recipes/ currently uses.
    "recipe": {
        "extras": {
            "code-friendly": None,
        },
        "safe_mode": "escape",
        "link_patterns": [
            # Transform "Recipe 123" in a link.
            #(re.compile(r"recipe\s+#?(\d+)\b", re.I),
            # r"http://code.activestate.com/recipes/\1/"),
        ],
        "extras": {
            "code-friendly": None,
            "pyshell": None,
            "demote-headers": 3,
            "link-patterns": None,
            # `class` attribute put on `pre` tags to enable using
            # <http://code.google.com/p/google-code-prettify/> for syntax
            # highlighting.
            "html-classes": {"pre": "prettyprint"},
            "cuddled-lists": None,
            "footnotes": None,
            "header-ids": None,
        },
        "safe_mode": "escape",
    }
}

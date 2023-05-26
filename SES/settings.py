from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-t+r#!p)4w29f^qvq%2z-wj6xe=pw#24$$q=4@1mo2#dnezm%&d'

DEBUG = True

ALLOWED_HOSTS = []



INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'student',
    'dashboard',
    'master_admin',
    'crispy_forms',
    "crispy_bootstrap5",
    'multiselectfield',
    'staff',
]
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'SES.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'SES.wsgi.application'


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# JAZZMIN Settings
JAZZMIN_SETTINGS = {
    "site_header": "SCS",
    "site_title": "SES",
    "site_brand": "SES",
    "default_ui": "django.contrib.admin",

    "index_title": "Site Administration",
    "table_small_menu": True,
    "table_small_menu_breakpoint": "md",
    "table_included_columns": {
        "auth.user": [
            "username",
            "email",
            "is_active",
            "is_staff",
            "date_joined",
        ],
        "yourapp.section": [  # Replace `yourapp` with your app name
            "id",
            "name",
            "description",
            "created_at",
        ],
    },
    "custom_css": None,
    "custom_js": None,
    "show_ui_builder": False,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": [],
    "collapsible_sidebar": False,
    "related_modal_active": False,
    "changeform_format_overrides": {},
    "fieldsets_formset_override": False,
    "changeform_format": "horizontal_tabs",  # horizontal_tabs, vertical_tabs, or single_column
    "exclude_django_admin_actions": False,
    "custom_search_fields": {},
    "custom_sortable_fields": {},
    "show_sidebar": True,
    "navigation_fixed": True,
    "show_count_in_sidebar": True,
    "navigation_expanded_css_classes": "col-md-2",
    "breadcrumbs_css_classes": "col-md-10",

}
JAZZMIN_UI_TWEAKS = {
    "theme": "darkly",
}
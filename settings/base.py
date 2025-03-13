from pathlib import Path
from dotenv import dotenv_values
from utils.constants import Settings
from os.path import join

config = dotenv_values(".env")


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config.get("SECRET_KEY")


# Application definition

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
PROJECT_APPS = ["pnr.apps.PnrConfig", "conf.apps.ConfConfig"]
THIRD_PARTY_APPS = ["channels", "django_extensions", "daphne"]
INSTALLED_APPS = THIRD_PARTY_APPS + DJANGO_APPS + PROJECT_APPS


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = Settings.ROOT_URLCONF

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [join(BASE_DIR, Settings.TEMPLATE_URL)],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = Settings.WSGI_APPLICATION
ASGI_APPLICATION = Settings.ASGI_APPLICATION

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = Settings.LANGUAGE_CODE

TIME_ZONE = Settings.TIME_ZONE

USE_I18N = Settings.USE_I18N

USE_TZ = Settings.USE_TZ


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = Settings.STATIC_URL
STATICFILES_DIRS = [join(BASE_DIR, Settings.STATICFILES_DIRS)]
STATIC_ROOT = Settings.STATIC_ROOT

MEDIA_ROOT = Settings.MEDIA_ROOT
MEDIA_URL = Settings.MEDIA_URL


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = Settings.DEFAULT_AUTO_FIELD


# Logging Configuration
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} - {asctime} - {name} - {message}",
            "style": "{",
        },
    },
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "debug.log",
            "formatter": "verbose",
        },
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console", "file"],
        "level": "INFO",
    },
}

# Railway Configuration Urls
# =====================================================
NTES_V1_BASE_URL = config.get("NTES_V1_BASE_URL")
NTES_V2_BASE_URL = config.get("NTES_V2_BASE_URL")
CAPTCHA_DRAW_URL = config.get("CAPTCHA_DRAW_URL")
TRAIN_ROUTE_URL = config.get("TRAIN_ROUTE_URL")
FETCH_TRAIN_DATA_URL = config.get("FETCH_TRAIN_DATA_URL")
PNR_STATUS_URL = config.get("PNR_STATUS_URL")

# Cache Configuration
# =====================================================
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "meri_rail_cache",
    }
}

# Mappls Api Configuration
MAPPLS_API_KEY = config.get("MAPPLS_API_KEY")

# Coogle Api Credentials Path
REDIRECT_URI = config.get("REDIRECT_URI")
CREDENTIALS_JSON = join(BASE_DIR, "fixtures/google/credentials.json")
TOKEN_JSON = join(BASE_DIR, "fixtures/google/token.json")
CLIENT_CONFIG = {
    "web": {
        "client_id": config.get("CLIENT_ID"),
        "client_secret": config.get("CLIENT_SECRET"),
        "auth_uri": config.get("AUTH_URI"),
        "token_uri": config.get("TOKEN_URI"),
    }
}
WEB_CLIENT_CONFIG = {
    "web": {
        "client_id": config.get("WEB_CLIENT_ID"),
        "client_secret": config.get("WEB_CLIENT_SECRET"),
        "auth_uri": config.get("AUTH_URI"),
        "token_uri": config.get("TOKEN_URI"),
    }
}
CREDENTIALS_CONFIG = {
    "token_uri": config.get("TOKEN_URI"),
    "client_id": config.get("CLIENT_ID"),
    "client_secret": config.get("CLIENT_SECRET"),
    "scopes": [
        "https://www.googleapis.com/auth/calendar.readonly",
        "https://www.googleapis.com/auth/calendar.events",
    ],
    "universe_domain": "googleapis.com",
}

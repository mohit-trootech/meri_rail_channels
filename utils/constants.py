from django.utils.translation import gettext_lazy as _  # noqa


class Settings:
    ROOT_URLCONF = "conf.urls"
    WSGI_APPLICATION = "conf.wsgi.application"
    ASGI_APPLICATION = "conf.asgi.application"

    LANGUAGE_CODE = "en-us"
    TIME_ZONE = "Asia/Kolkata"
    USE_I18N = True
    USE_TZ = True

    # Static Files & Media Files
    TEMPLATE_URL = "templates"
    STATIC_URL = "/static/"
    STATICFILES_DIRS = "templates/static"
    MEDIA_URL = "/media/"
    STATIC_ROOT = "static"
    MEDIA_ROOT = "media"

    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


class AppLabelsModels:
    pass

from django.utils.translation import gettext_lazy as _  # noqa

CONFIGURED_CAPTCHA = "0"
NOT_CONFIGURE_CAPTCHA = "1"


class Fixtures:
    PAGE_SS = "fixtures/temp/page_screenshot.png"


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
    # app_name: pnr
    PNR_STATUS = {
        "app_label": "pnr",
        "model_name": "PnrStatus",
    }
    REQUEST_TYPE = {
        "app_label": "conf",
        "model_name": "RequestType",
    }
    SEAT_STATUS = {
        "app_label": "seat",
        "model_name": "SeatStatus",
    }
    FARE_STATUS = {
        "app_label": "fare",
        "model_name": "FareStatus",
    }


class SeleniumServices:
    """Selenium Services"""

    PNR_STATUS = "pnr_status"
    FARE_ENQUIRY = "fare_enquiry"
    TRAIN_SCHEDULE = "train_schedule"
    SPOT_TRAIN = "spot_train"
    SEAT_AVAILABILITY = "seat_availability"


class ErrorMessages:
    NOT_DEFINED = "%s is not defined as class atrribute"
    UNABLE_TO_PROCESS_TRY_AGAIN_LATER = _(
        "Unable to process your request. Please try again later."
    )
    MODEL_IS_NONE = NOT_DEFINED % "Model"
    SERVICE_IS_NONE = NOT_DEFINED % "Service"
    FILTER_SERIALIZER_IS_NONE = NOT_DEFINED % "Filter Serializer"
    CHOICE_CLASS_NOT_SET = _("Choice Class Not Set")
    INVALID_SERVICE = _("Invalid Service Defined")


class ValidationErrorConstants:
    DATE_IN_PAST = _("Date must be greater than or equal to today")
    STATION_NOT_FOUND = _("Station not found")
    TRAIN_NOT_FOUND = _("Train not found")
    FROM_TO_STATION_SAME = _("From and to station cannot be same")
    DATE_AFTER_THREE_MONTHS = _("Date cannot be more than 3 months from today")
    INVALID_TRAIN_NUMBER = _("Train number is invalid")


# NTES Configuration Constants
class UrlTypesV1:
    """NTES V1 Url Types"""

    FETCH_TRAIN_DATA = "FetchTrainData"
    CATPCHA_DRAW = "captchaDraw.png"
    CAPTCHA_CONFIG = "CaptchaConfig"


class UrlsV1:
    """NTES V1 Urls"""

    CAPTCHA_CONFIG = "%s"
    CAPTCHA_DRAW = "%s?%s"
    TRAIN_SCHEDULE = "CommonCaptcha?inputCaptcha=%(captcha)s&trainNo=%(train)s&inputPage=TRAIN_SCHEDULE&language=en&_=%(time)s"
    PNR_STATUS = "CommonCaptcha?inputCaptcha=%(captcha)s&inputPnrNo=%(pnr)s&inputPage=PNR&language=en"
    FARE = "CommonCaptcha?inputCaptcha=%(captcha)s&trainNo=%(train)s&dt=%(dt)s&sourceStation=%(from_station)s&destinationStation=%(to_station)s&classc=%(train_cls)s&quota=%(quota)s&inputPage=FARE&language=en&_=%(time)s"
    TRAIN_BETWEEN_STATIONS = "CommonCaptcha?inputCaptcha=%(captcha)s&dt=%(dt)s&sourceStation=%(from_station)s&destinationStation=%(to_station)s&flexiWithDate=n&inputPage=TBIS&language=en&_=%(time)s"
    SEAT_AVAILABILITY = "CommonCaptcha?inputCaptcha=%(captcha)s&trainNo=%(train)s&dt=%(dt)s&sourceStation=%(from_station)s&destinationStation=%(to_station)s&classc=%(train_cls)s&quota=%(quota)s&inputPage=SEAT&language=en&_=%(time)s"


class Timeout:
    """Timeout Constants"""

    FIVE_SECONDS = 5
    TEN_SECONDS = 10
    THIRTY_SECONDS = 30
    FIFTY_SECONDS = 50
    SIXTY_SECONDS = 60
    ONE_HUNDRED_SECONDS = 100
    TWO_HUNDRED_SECONDS = 200
    FIVE_HUNDRED_SECONDS = 500

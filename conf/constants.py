from django.utils.translation import gettext_lazy as _


class RequestTypes:
    PNR = "PNR"
    TRAIN_ROUTE = "TRAIN_ROUTE"
    LIVE_STATUS = "LIVE_STATUS"
    TRAIN_BETWEEN_STATIONS = "TRAIN_BETWEEN_STATIONS"
    TRAIN_SCHEDULE = "TRAIN_SCHEDULE"
    SEAT_AVAILABILITY = "SEAT_AVAILABILITY"
    FARE_ENQUIRY = "FARE_ENQUIRY"
    CANCELLED_TRAINS = "CANCELLED_TRAINS"
    RESCHEDULED_TRAINS = "RESCHEDULED_TRAINS"
    DIVERTED_TRAINS = "DIVERTED_TRAINS"
    STATION_STATUS = "STATION_STATUS"

    CHOICES = (
        (PNR, _("PNR")),
        (TRAIN_ROUTE, _("Train Route")),
        (LIVE_STATUS, _("Live Status")),
        (TRAIN_BETWEEN_STATIONS, _("Train Between Station")),
        (TRAIN_SCHEDULE, _("Train Schedule")),
        (SEAT_AVAILABILITY, _("Seat Availability")),
        (FARE_ENQUIRY, _("Fare Enquiry")),
        (CANCELLED_TRAINS, _("Cancelled Trains")),
        (RESCHEDULED_TRAINS, _("Rescheduled Trains")),
        (DIVERTED_TRAINS, _("Diverted Trains")),
        (STATION_STATUS, _("Station Status")),
    )

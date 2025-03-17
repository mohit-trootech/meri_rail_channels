from utils.base_service import Service
from utils.constants import AppLabelsModels, SeleniumServices
from utils.utils import get_model


class SeatService(Service):
    model = get_model(**AppLabelsModels.SEAT_STATUS)
    service = SeleniumServices.SEAT_AVAILABILITY

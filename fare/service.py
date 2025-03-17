from utils.base_service import Service
from utils.constants import AppLabelsModels, SeleniumServices
from utils.utils import get_model


class FareService(Service):
    model = get_model(**AppLabelsModels.FARE_STATUS)
    service = SeleniumServices.FARE_ENQUIRY

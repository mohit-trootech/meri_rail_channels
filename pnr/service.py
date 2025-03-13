from utils.base_service import Service
from utils.constants import AppLabelsModels, SeleniumServices
from utils.utils import get_model


class PnrService(Service):
    model = get_model(**AppLabelsModels.PNR_STATUS)
    service = SeleniumServices.PNR_STATUS

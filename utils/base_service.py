from utils.selenium_service import SeleniumService
from utils.constants import SeleniumServices, ErrorMessages
from json import loads


class Service:
    selenium_service = SeleniumService
    service = None
    model = None
    driver = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.model is None:
            raise ValueError(ErrorMessages.MODEL_IS_NONE)
        if self.service is None:
            raise ValueError(ErrorMessages.SERVICE_IS_NONE)

    def get_service_method(self):
        if SeleniumServices.PNR_STATUS == self.service:
            return self.driver.load_pnr_details
        elif SeleniumServices.FARE_ENQUIRY == self.service:
            return self.driver.fare_enquiry
        elif SeleniumServices.SPOT_TRAIN == self.service:
            return self.driver.spot_train_details
        elif SeleniumServices.SEAT_AVAILABILITY == self.service:
            return self.driver.seat_availability
        raise ValueError(ErrorMessages.INVALID_SERVICE)

    def use_selenium(self, data: dict):
        self.driver = self.selenium_service()
        captcha = self.driver.configure_captcha()
        service_method = self.get_service_method()
        data = loads(service_method(captcha, data))
        return data

    def get_object(self, data):
        try:
            return self.model.objects.get(**data)
        except self.model.DoesNotExist:
            return None

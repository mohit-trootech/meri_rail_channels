from utils.utils import get_model
from utils.constants import AppLabelsModels
from django.contrib.admin import ModelAdmin

PnrStatus = get_model(**AppLabelsModels.PNR_STATUS)


class PnrStatusAdmin(ModelAdmin):
    list_display = ["pnr", "created"]

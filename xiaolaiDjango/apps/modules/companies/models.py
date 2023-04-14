from django.db import models
from apps.utils.base_model import BaseModel


class Companies(BaseModel):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    bc_id = models.IntegerField(null=True, blank=True)

    class Meta:
        de_table = "companies"
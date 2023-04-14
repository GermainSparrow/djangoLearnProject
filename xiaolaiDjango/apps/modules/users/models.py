from enum import IntEnum

from django.db import models
from apps.utils.base_model import BaseModel
from apps.modules.companies.models import Companies


# Create your models here.

class UseEnum(IntEnum):
    ADMIN = 0
    SENIOR_BUYER = 1
    JUNIOR_BUYER = 2
    SUPER_ADMIN = 3

    @classmethod
    def choice(cls):
        return tuple((i.value, i.name for i in cls))


class User(BaseModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    bc_id = models.IntegerField(null=True, blank=True)
    company_id = models.ForeignKey(Companies, related_name="company_users", on_delete=models.CASCADE(''))
    role = models.SmallIntegerField()

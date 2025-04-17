from decimal import Decimal
from django.conf import settings
from django.db import models
# import shop.models

class Cart(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    def __str__(self):
        return self.name

class Carts(object):
    pass
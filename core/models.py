from django.db import models
from django.utils.translation import gettext_lazy as _


class ProductModel(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Product Name'))
    description = models.TextField(verbose_name=_('Product Description'))

    def __str__(self):
        return f'{self.name}'
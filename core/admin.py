from django.contrib import admin
from .models import ProductModel


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(ProductModel, ProductAdmin)    
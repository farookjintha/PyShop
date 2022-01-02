from django.contrib import admin

import products
from .models import Product, Offer

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)

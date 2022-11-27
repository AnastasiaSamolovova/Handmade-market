from django.contrib import admin
from offers.models import Offer


@admin.register(Offer)
class ProductAdmin(admin.ModelAdmin):
    list_display = "pk", "product", "color", "price", "slug"
    list_display_links = "pk", "product"

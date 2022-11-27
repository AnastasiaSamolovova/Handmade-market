from django.contrib import admin
from products.models import Color, Category, Product


@admin.register(Color, Category)
class UniversalAdmin(admin.ModelAdmin):
    list_display = "pk", "name"
    list_display_links = "pk", "name",


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "category"
    list_display_links = "pk", "name"

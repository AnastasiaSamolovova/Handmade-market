from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404

from .models import Product


def index(request: HttpRequest):
    context = {
        "products": (
            Product
            .objects
            .select_related("category")
            .order_by("pk")
            .all()
        ),
    }
    return render(request=request, template_name="products/index.html", context=context)


def details(request: HttpRequest, pk: int):
    product = get_object_or_404(
        (
            Product
            .objects
            .select_related("category")
        ),
        pk=pk,
    )
    context = {
        "product": product,
    }
    return render(request=request, template_name="products/details.html", context=context)

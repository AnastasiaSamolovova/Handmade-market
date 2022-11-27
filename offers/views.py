from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404

from .models import Offer


def index(request: HttpRequest):
    context = {
        "offers": (
            Offer
            .objects
            .select_related("product", "product__category")
            .order_by("pk")
            .all()
        ),
    }
    return render(request=request, template_name="offers/index.html", context=context)


def details(request: HttpRequest, pk: int):
    offer = get_object_or_404(
        (
            Offer
            .objects
            .select_related("product", "product__category")
        ),
        pk=pk,
    )
    context = {
        "offer": offer,
    }
    return render(request=request, template_name="offers/details.html", context=context)

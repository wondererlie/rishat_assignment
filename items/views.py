import stripe
from django.conf import settings
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.views import View

from items.models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


class BuyItemView(View):
    def get(self, request: HttpRequest, pk: int):
        item = get_object_or_404(Item, pk=pk)

        line_items = [
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {
                        "name": item.name,
                    },
                    "unit_amount": int(item.price * 100),
                },
                "quantity": 1,
            }
        ]

        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=line_items,
            mode="payment",
            success_url="http://localhost:8000/",
            cancel_url="http://localhost:8000/",
        )

        return JsonResponse({"session_id": session.id})


class ItemView(View):
    def get(self, request: HttpRequest, pk: int):
        item = get_object_or_404(Item, pk=pk)
        html = render_to_string(
            "item.html",
            {
                "item": item,
                "stripe_public_key": settings.STRIPE_PUBLIC_KEY,
            },
        )
        return HttpResponse(html)

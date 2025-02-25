from django.urls import path

from items.views import BuyItemView, ItemView

urlpatterns = [
    path("buy/<int:pk>/", BuyItemView.as_view(), name="buy_item"),
    path("item/<int:pk>/", ItemView.as_view(), name="item_detail"),
]

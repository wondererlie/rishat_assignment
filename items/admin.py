from django.contrib import admin

from items.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    fields = "name", "description", "price"
    list_display = "id", "name", "price"
    list_display_links = "id", "name"
    ordering = "-id", "-name"
    list_per_page = 50
    search_fields = (
        "id",
        "name",
    )

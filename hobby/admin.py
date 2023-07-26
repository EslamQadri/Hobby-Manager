from django.contrib import admin

# Register your models here.
from hobby.models import Hobby, HobbyProgress, Product


@admin.register(Hobby)
class HoppyAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "hobby", "note", "days_of_hobby")


@admin.register(HobbyProgress)
class HobbyProgressAdmin(admin.ModelAdmin):
    list_display = ("id", "hobby", "day", "is_completed", "created_at", "updated_at")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product",
        "size",
        "sell_price",
        "buy_price",
        "Quantity",
        "barcode",
    )

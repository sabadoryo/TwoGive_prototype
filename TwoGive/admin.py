import decimal

from django.contrib import admin

# Register your models here.
from TwoGive.models import authUser, Item, Cart
#
#
# class EntryAdmin(admin.ModelAdmin):
#     # Overide of the save model
#     def save_model(self, request, obj, form, change):
#         obj.cart.total += decimal.Decimal(decimal.Decimal(obj.quantity) * decimal.Decimal(obj.item.price))
#         obj.cart.count += obj.quantity
#         obj.cart.save()
#         super().save_model(request, obj, form, change)


admin.site.register(authUser)
admin.site.register(Item)
admin.site.register(Cart)
# admin.site.register(Entry, EntryAdmin)

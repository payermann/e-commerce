from .models import Product, Action
from django.contrib import admin

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')

admin.site.register(Product, ProductAdmin)

class ActionAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Action, ActionAdmin)
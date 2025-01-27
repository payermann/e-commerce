from .models import Product
from django.contrib import admin

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')

admin.site.register(Product, ProductAdmin)

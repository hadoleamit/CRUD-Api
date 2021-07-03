from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['category']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['product_name','category','price']
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Product,Image,Category
# # Register your models here.
# class PictureInline(admin.StackedInline):
#     model = Image
class ProductAdmin(ModelAdmin):
    list_display=['title','price']
    # inlines = [PictureInline]

class ProductInline(admin.StackedInline):
    model = Product
    extra=0
class CategoryAdmin(ModelAdmin):
    inlines = [ProductInline]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
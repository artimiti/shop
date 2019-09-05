from django.contrib import admin
from .models import *


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductCategoryAdm (admin.ModelAdmin):
    list_display = [field.name for field in ProductCategory._meta.fields]
    
    class Meta:
        model = ProductCategory

admin.site.register(ProductCategory, ProductCategoryAdm)


class ProductAdm (admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImageInline]

    class Meta:
        model = Product

admin.site.register(Product, ProductAdm)


class ProductImageAdm (admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]

    class Meta:
        model = ProductImage

admin.site.register(ProductImage, ProductImageAdm)

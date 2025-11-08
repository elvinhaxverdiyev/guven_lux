from django.contrib import admin
from guvenluxapp.models.background_image import BackgroundImage
from guvenluxapp.models.product_image import ProductImage
from guvenluxapp.forms import ProductImageInlineFormSet
from guvenluxapp.models.products import Product


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    formset = ProductImageInlineFormSet
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'main_category', 'sub_category', 'price', 'is_active', 'is_popular']
    list_filter = ['main_category', 'sub_category', 'is_active', 'is_popular']
    search_fields = ['name']
    inlines = [ProductImageInline] 

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
    list_display = ('name', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)
    inlines = [ProductImageInline]
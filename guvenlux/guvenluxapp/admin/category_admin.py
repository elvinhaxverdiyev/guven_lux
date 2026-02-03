from django.contrib import admin
from guvenluxapp.models.category import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_category')
    list_filter = ('parent_category',)
    search_fields = ('name',)

    class Media:
        js = ('assets/js/admin_image_compress.js',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "parent_category":
            kwargs["queryset"] = Category.objects.filter(parent_category__isnull=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

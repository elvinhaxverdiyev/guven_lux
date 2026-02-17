from django.contrib import admin
from django.utils.html import format_html
from ..models.company import Company  # Company modelini import et

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo_preview')  # ad və logo önizləməsi
    readonly_fields = ('logo_preview',)     # logo önizləməsi readonly olsun
    search_fields = ('name',)               # şirkət adına görə axtarış
    list_filter = ()                        # lazım olsa filtrlər əlavə edə bilərsən

    class Media:
        js = ('assets/js/admin_image_compress.js',)

    def logo_preview(self, obj):
        if obj.logo:
            return format_html(
                '<img src="{}" width="80" height="80" style="object-fit: contain; border-radius: 5px;" />',
                obj.logo.url
            )
        return "-"
    logo_preview.short_description = 'Logo Önizləmə'

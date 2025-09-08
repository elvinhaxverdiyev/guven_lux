from django.contrib import admin
from django.utils.html import format_html
from ..models.employee import Employee
from ..models.company import Company 


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo_preview')
    readonly_fields = ('photo_preview',)
    exclude = ('position', 'phone', 'company',)
    search_fields = ('name', 'company__name')
    list_filter = ('company',)

    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="60" height="60" style="object-fit: cover; border-radius: 5px;" />', obj.photo.url)
        return "-"
    photo_preview.short_description = 'Şəkil Önizləmə'

    def save_model(self, request, obj, form, change):
        if not obj.company:
            obj.company = Company.objects.first()  # və ya default şirkət
        super().save_model(request, obj, form, change)

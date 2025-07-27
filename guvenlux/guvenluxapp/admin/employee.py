from django.contrib import admin
from ..models import Employee


class EmployeeInline(admin.TabularInline):
    model = Employee
    extra = 1


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'company')

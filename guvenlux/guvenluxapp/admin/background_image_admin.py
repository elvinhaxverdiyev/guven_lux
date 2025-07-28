from django.contrib import admin
from guvenluxapp.models.background_image import BackgroundImage

@admin.register(BackgroundImage)
class BackgroundImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'page', 'image', 'created_at')  # page əlavə edildi
    list_filter = ('page', 'created_at')  # page üzrə süzgəc əlavə edildi
    search_fields = ('id', 'title')  # title üzrə də axtarış əlavə etmək olar

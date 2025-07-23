from django.db import models


class BackgroundImage(models.Model):
    image = models.ImageField(
        upload_to='background_images',
        verbose_name='Arxa plan şəkli'
        )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    
    def __str__(self):
        return f'Şəkil #{self.id}'
    
    class Meta:
        verbose_name = 'Arxa plan şəkli'
        verbose_name_plural = 'Arxa plan şəkilləri'
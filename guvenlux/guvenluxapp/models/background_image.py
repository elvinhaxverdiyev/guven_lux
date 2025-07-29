from django.db import models


class BackgroundImage(models.Model):
    PAGE_CHOICES = [
        ('index', 'Ana Sehife'),
        ('about', 'Haqqimizda'),
        ('contact', 'Bizimle Elaqe'),
        ('subcategory', 'Alt Kategorya Sehifesi'),
        ('products_detail', 'Mehsul Sehifesi'),
        ('products_list', 'Filterlenmis mehsullar shifesi')
    ]
    page = models.CharField(max_length=20, choices=PAGE_CHOICES, default='index')
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='background_images', verbose_name='Arxa plan şəkli')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Şəkil #{self.id} - {self.page}'

    class Meta:
        verbose_name = 'Arxa plan şəkli'
        verbose_name_plural = 'Arxa plan şəkilləri'

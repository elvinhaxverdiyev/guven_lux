from django.db import models
from django.utils.text import slugify

from .category import Category


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='products',
        verbose_name='Kateqoriya'
    )
    name = models.CharField(
        max_length=150,
        verbose_name='Ad'
    )
    description = models.TextField(
        max_length=500,
        verbose_name='Haqqında'
    )
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True)

    price = models.FloatField(
        verbose_name='Qiymət'   
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Məhsul aktivliyi'
    )
    is_popular = models.BooleanField(
        default=False,
        verbose_name = 'Ana səhifədə olacaq seçili məhsul'
    )

    def get_main_image_url(self):
        first_image = self.images.first()
        if first_image and first_image.image:
            return first_image.image.url

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Məhsul'
        verbose_name_plural = 'Məhsullar'
    
   
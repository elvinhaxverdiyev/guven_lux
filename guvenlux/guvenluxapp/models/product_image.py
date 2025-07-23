from django.db import models
from django.core.exceptions import ValidationError

from .products import Product


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Məhsul',
    )
    image = models.ImageField(
        upload_to='product_images',
        verbose_name='Məhsul şəkli',
        null=True,
        blank=True
        )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'Image#{self.id} of {self.product.name}'
    
    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return ''
    
    def clean(self):
        if self.product and self.product.pk:
            if self.product.images.count() >= 3 and not self.pk:
                raise ValidationError('Məhsula maksimum 3 şəkil əlavə etmək olar.')
    
    def save(self, *args, **kwargs):
        self.full_clean() 
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Məhsul şəkli'
        verbose_name_plural = 'Məhsul şəkilləri'
    
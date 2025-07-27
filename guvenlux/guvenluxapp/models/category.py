from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    parent_category = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name='Əsas kateqoriya'
    )
    name = models.CharField(max_length=150, verbose_name='Ad')
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True)  # yeni sahə əlavə olundu
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

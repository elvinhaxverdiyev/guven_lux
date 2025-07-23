from django.db import models


class Category(models.Model):
    parent_category = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name='Əsas kateqoriya'
    )
    name = models.CharField(
        max_length=150,
        verbose_name='Ad'
    )
   
    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = 'Kateqoriya'
        verbose_name_plural = 'Kateqoriyalar'
    
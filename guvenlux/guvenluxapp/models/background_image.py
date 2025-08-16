from django.db import models


class BackgroundImage(models.Model):
    """
    Model representing background images for different pages of the website.

    Attributes:
        PAGE_CHOICES (list[tuple]): List of available page types where the background image can be used.
        page (str): Page identifier where the background image will be displayed.
        title (str): Optional title for the background image.
        description (str): Optional description for the background image.
        image (ImageField): The uploaded background image file.
        created_at (datetime): Date and time when the image was added.
    """
    
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
        """Return a human-readable string representation of the background image."""
        return f'Şəkil #{self.id} - {self.page}'

    class Meta:
        verbose_name = 'Arxa plan şəkli'
        verbose_name_plural = 'Arxa plan şəkilləri'

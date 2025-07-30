from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Shirket'
        verbose_name_plural = 'Shirketler'
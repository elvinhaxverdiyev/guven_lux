from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="companies/", blank=True, null=True)  # əgər logo da lazım olsa

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tərəfdaş"
        verbose_name_plural = "Tərəfdaşlar"

from django.shortcuts import render
from django.views import View


from guvenluxapp.models import (
    BackgroundImage
)

__all__ = [
    'Contactiew'  
]


class Contactiew(View):
    def get(self, request):
        bg_image = BackgroundImage.objects.filter(page='contact').order_by('-id').first()
        return render(request, 'contact.html', {'bg_image': bg_image})

from django.shortcuts import render
from django.views import View


from guvenluxapp.models import (
    BackgroundImage
)

__all__ = [
    'Contactiew'  
]


class Contactiew(View):
    """
    View for rendering the contact page.

    Retrieves:
    - The latest background image for the 'contact' page based on the highest ID.

    Context sent to the template:
    - bg_image: The most recently added BackgroundImage object for the 'contact' page.

    Template:
    - contact.html
    """
    def get(self, request):
        bg_image = BackgroundImage.objects.filter(page='contact').order_by('-id').first()
        return render(request, 'contact.html', {'bg_image': bg_image})

from django.shortcuts import render
from django.views import View

from guvenluxapp.models import (
    Product,
    BackgroundImage
)

__all__ = [
    'HomePageView'  
]

class HomePageView(View):
    def get(self, request):
        background_images = BackgroundImage.objects.filter(page='index').order_by('-created_at')
        popular_products = Product.objects.filter(
            is_active=True, is_popular=True
            ).order_by('-created_at')
        
        return render(request, 'index.html', {
            'popular_products': popular_products,
            'background_images': background_images
            })

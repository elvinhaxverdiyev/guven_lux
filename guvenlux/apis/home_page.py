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
    """
    Home Page View.

    Handles GET requests for the homepage by fetching data from the database
    and rendering it to the `index.html` template.

    Data retrieved:
        - background_images (QuerySet): Background images from the `BackgroundImage` model
          filtered by `page='index'`, ordered by creation date (newest first).
        - popular_products (QuerySet): Active (`is_active=True`) and popular (`is_popular=True`)
          products from the `Product` model, ordered by creation date (newest first).

    Template:
        index.html

    Context:
        popular_products (QuerySet): List of popular products.
        background_images (QuerySet): Background images for the homepage.
    """
    def get(self, request):
        background_images = BackgroundImage.objects.filter(page='index').order_by('-created_at')
        popular_products = Product.objects.filter(
            is_active=True, is_popular=True
            ).order_by('-created_at')
        
        return render(request, 'index.html', {
            'popular_products': popular_products,
            'background_images': background_images
            })

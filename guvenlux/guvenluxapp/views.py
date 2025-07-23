from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views import View


from guvenluxapp.models import (
    Product,
    Category,
    BackgroundImage,
)

__all__ = [
    'HomePageView',

]

class HomePageView(View):
    def get(self, request):
        background_images = BackgroundImage.objects.all()
        popular_products = Product.objects.filter(
            is_active=True, is_popular=True
            ).order_by('-created_at')
        
        return render(request, 'index.html', {
            'popular_products': popular_products,
            'background_images': background_images
            })


def products_list(request):
    return render(request, 'products_list.html')

def blog_list(request):
    return render(request, 'blog_list.html')

def about_page(request):
    return render(request, 'about.html')
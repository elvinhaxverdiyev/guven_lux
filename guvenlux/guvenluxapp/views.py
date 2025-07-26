from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views import View
from django.core.paginator import Paginator
from django.views.generic import DetailView
from django.http import JsonResponse

from guvenluxapp.models import (
    Product,
    Category,
    BackgroundImage,
)

__all__ = [
    'HomePageView',
    'ProductDetailView',
    'ProductPageView',
    'SubcategoryListView',
    'CategoryDetailView'

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


class CategoryDetailView(DetailView):
    model = Category
    context_object_name = 'category'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class ProductPageView(View):
    def get(self, request):
        products_list  = Product.objects.filter(is_active=True).order_by('-created_at')
        category = Category.objects.all()
        categories = Category.objects.filter(parent_category=None)
        paginator = Paginator(products_list, 9)  
        page_number = request.GET.get('page')
        products = paginator.get_page(page_number)

        return render(request, 'product.html', {
            'products': products,
            'categories': categories,
            'category': category,
            'paginator': paginator,
            'page_obj': products, 
            })


class ProductDetailView(View):
    def get(self, request, product_slug):
        product = get_object_or_404(Product, slug=product_slug)
        categories = Category.objects.filter(parent_category=None)

        return render(request, 'product-detail.html', {
            'product': product,
            'categories': categories
            })


class SubcategoryListView(View):
    def get(self, request, category_slug):
        parent_category = get_object_or_404(Category, slug=category_slug)
        subcategories = Category.objects.filter(parent_category=parent_category)

        return render(request, 'subcategory.html', {
            'parent_category': parent_category,
            'subcategories': subcategories
        })

def contact(request):
    return render(request, 'contact.html')

def about_page(request):
    return render(request, 'about.html')
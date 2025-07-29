# guvenlux/guvenluxapp/views.py
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views import View
from django.core.paginator import Paginator
from django.views.generic import DetailView
from django.http import JsonResponse
from django.views.generic import ListView
from django.db.models import Q

from guvenluxapp.models import (
    Product,
    Category,
    BackgroundImage,
    Company
)

__all__ = [
    'HomePageView',
    'ProductDetailView',
    'SubcategoryListView',
    'CategoryDetailView',
    "CompanyOverviewView" ,
    'ProductsListView'   
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



class CategoryDetailView(DetailView):
    model = Category
    context_object_name = 'category'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


        
class ProductsListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products_list.html'

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Product.objects.filter(
            Q(main_category__slug=slug) | Q(sub_category__slug=slug)
        )
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subcategory'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context


class ProductDetailView(View):
    def get(self, request, product_slug):
        product = get_object_or_404(Product, slug=product_slug)
        categories = Category.objects.filter(parent_category=None)
        bg_image = BackgroundImage.objects.filter(page='products_detail').order_by('-id').first()
        return render(request, 'product_detail.html', {
            'product': product,
            'categories': categories,
            'bg_image': bg_image
        })

class SubcategoryListView(View):
    def get(self, request, category_slug):
        parent_category = get_object_or_404(Category, slug=category_slug)
        subcategories = Category.objects.filter(parent_category=parent_category)
        bg_image = BackgroundImage.objects.filter(page='subcategory').order_by('-id').first()

        return render(request, 'subcategory.html', {
            'parent_category': parent_category,
            'subcategories': subcategories,
            'bg_image': bg_image
        })


class CompanyOverviewView(View):
    def get(self, request):
        companies = Company.objects.prefetch_related('employees').all()
        bg_image = BackgroundImage.objects.filter(page='about').order_by('-created_at').first()
        return render(request, 'about.html', {
            'companies': companies,
            'bg_image': bg_image,
        })


def contact(request):
    bg_image = BackgroundImage.objects.filter(page='contact').order_by('-id').first()
    return render(request, 'contact.html', {'bg_image': bg_image})
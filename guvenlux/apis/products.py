# guvenlux/guvenluxapp/views.py
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import ListView
from django.db.models import Q

from guvenluxapp.models import (
    Product,
    Category,
    BackgroundImage,
)

__all__ = [
    'ProductDetailView',
    'ProductsListView'   
]

        
class ProductsListView(ListView):
    """
    Displays a list of products filtered by category slug.

    Retrieves products that match either the main category slug
    or the subcategory slug passed in the URL.

    Template:
        products_list.html

    Context:
        products (QuerySet): The filtered list of products.
        subcategory (Category): The category object for the given slug.
        background_image (BackgroundImage or None): Background image for the products list page.
    """
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
        bg_image = BackgroundImage.objects.filter(page='products_list').order_by('-created_at').first()
        context['background_image'] = bg_image
        
        return context


class ProductDetailView(View):
    """
    Displays detailed information for a single product.

    Retrieves the product based on the `product_slug` provided in the URL,
    along with all top-level categories and a background image for the detail page.

    Template:
        product_detail.html

    Context:
        product (Product): The product object being viewed.
        categories (QuerySet): All top-level categories.
        bg_image (BackgroundImage or None): Background image for the product detail page.
    """
    def get(self, request, product_slug):
        product = get_object_or_404(Product, slug=product_slug)
        categories = Category.objects.filter(parent_category=None)
        bg_image = BackgroundImage.objects.filter(page='products_detail').order_by('-id').first()
        return render(request, 'product_detail.html', {
            'product': product,
            'categories': categories,
            'bg_image': bg_image
        })

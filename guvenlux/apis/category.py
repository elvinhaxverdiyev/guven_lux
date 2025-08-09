from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import DetailView


from guvenluxapp.models import (
    Category,
    BackgroundImage,
)

__all__ = [
    'SubcategoryListView',
    'CategoryDetailView'  
]


class CategoryDetailView(DetailView):
    """
    DetailView to display a specific Category object
    identified by slug in the URL.
    """
    model = Category
    context_object_name = 'category'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


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

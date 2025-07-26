# yourapp/context_processors.py

from guvenluxapp.models import Category

def main_categories(request):
    # Yalnız əsas kateqoriyalar (parent_category=None)
    return {
        'main_categories': Category.objects.filter(parent_category=None).prefetch_related('children')
    }

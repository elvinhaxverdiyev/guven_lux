from guvenluxapp.models import Category

def main_categories(request):
    """
    Context processor that returns all main (top-level) categories with their related child categories.
    
    This function filters categories that have no parent_category (i.e., top-level categories)
    and prefetches their related 'children' to optimize database queries.
    
    Args:
        request (HttpRequest): The incoming HTTP request object.

    Returns:
        dict: A context dictionary containing 'main_categories' for use in templates.
    """
    return {
        'main_categories': Category.objects.filter(parent_category=None).prefetch_related('children')
    }

from django.shortcuts import render
from django.views import View

from guvenluxapp.models import (
    BackgroundImage,
    Company
)

__all__ = [
    "CompanyOverviewView" 
]


class CompanyOverviewView(View):
    """
    View for displaying the company overview page.

    Retrieves:
    - All companies
    - The latest background image for the 'about' page.

    Context sent to the template:
    - companies: QuerySet of Company objects
    - bg_image: The most recently created BackgroundImage for the 'about' page.

    Template:
    - about.html
    """
    def get(self, request):
        companies = Company.objects.all()
        bg_image = BackgroundImage.objects.filter(page='about').order_by('-created_at').first()
        return render(request, 'about.html', {
            'companies': companies,
            'bg_image': bg_image,
        })

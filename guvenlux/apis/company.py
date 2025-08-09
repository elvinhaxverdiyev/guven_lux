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
    def get(self, request):
        companies = Company.objects.prefetch_related('employees').all()
        bg_image = BackgroundImage.objects.filter(page='about').order_by('-created_at').first()
        return render(request, 'about.html', {
            'companies': companies,
            'bg_image': bg_image,
        })

from django.urls import path
from . import views
from .views import *


urlpatterns = [
   path(
        '', 
        HomePageView.as_view(), 
        name='index'
    ),
   
   path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category-detail'),

   
   path(
        'products/', 
        ProductPageView.as_view(), 
        name='product-list'
    ),
    path(
        'product/<slug:product_slug>/', 
        ProductDetailView.as_view(), 
        name='product-detail'
    ),
    path('category/<slug:category_slug>/subcategories/', SubcategoryListView.as_view(), name='subcategories-by-category'),

    path('about/', CompanyOverviewView.as_view(), name='about-page'),

    path('contact/', views.contact, name='contact-page'),
    path('about/', views.about_page, name='about-page'),
]

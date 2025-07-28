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
        'product/<slug:product_slug>/', 
        ProductDetailView.as_view(), 
        name='product-detail'
    ),
    path('category/<slug:category_slug>/subcategories/', SubcategoryListView.as_view(), name='subcategories-by-category'),
    path('subcategory/<slug:slug>/', ProductsListView.as_view(), name='products-by-subcategory'),

    path('about/', CompanyOverviewView.as_view(), name='about-page'),

    path('contact/', views.contact, name='contact-page'),
]

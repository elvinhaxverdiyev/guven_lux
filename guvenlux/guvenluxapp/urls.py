from django.urls import path
from . import views
from .views import *


urlpatterns = [
   path(
        '', 
        HomePageView.as_view(), 
        name='index'
    ),
    path('products/', views.products_list, name='products-list'),
    path('blogs/', views.blog_list, name='blog-list'),
    path('about/', views.about_page, name='about-page'),
]

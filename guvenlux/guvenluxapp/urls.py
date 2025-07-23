from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.index,
        name='index'
    ),
    path('products/', views.products_list, name='products-list'),
    path('blogs/', views.blog_list, name='blog-list'),
    path('about/', views.about_page, name='about-page'),
]

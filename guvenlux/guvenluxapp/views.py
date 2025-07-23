from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def products_list(request):
    return render(request, 'products_list.html')

def blog_list(request):
    return render(request, 'blog_list.html')

def about_page(request):
    return render(request, 'about.html')
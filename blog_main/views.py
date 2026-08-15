
from django.shortcuts import render
# from django.http import HttpResponse
# from ../templates import *
from blogs.models import Category, Blog

def home(request):
    categories = Category.objects.all()
    featured_post = Blog.objects.filter(is_featured=True, status='Published').order_by('updated_at')
    recent_post =  Blog.objects.filter(is_featured=False, status='Published').order_by('updated_at')
    context = {
        'categories': categories,
        'featured_post': featured_post,
        'recent_post': recent_post,
    }
    print(recent_post)
    return render(request, 'home.html', context)
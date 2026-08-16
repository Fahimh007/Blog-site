
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from blogs.models import Category, Blog


def home(request):
    categories = Category.objects.all()
    featured_post = Blog.objects.filter(is_featured=True, status='Published').order_by('updated_at')
    recent_post = Blog.objects.filter(is_featured=False, status='Published').order_by('updated_at')
    context = {
        'categories': categories,
        'featured_post': featured_post,
        'recent_post': recent_post,
    }
    return render(request, 'home.html', context)


def search(request):
    keyword = request.GET.get('keyword', '')
    posts = Blog.objects.filter(status='Published', title__icontains=keyword).order_by('updated_at') if keyword else Blog.objects.none()
    context = {
        'categories': Category.objects.all(),
        'recent_post': posts,
        'keyword': keyword,
    }
    return render(request, 'home.html', context)


def login_view(request):
    return redirect('home')


def register_view(request):
    return redirect('home')


def dashboard(request):
    return redirect('home')


def logout_view(request):
    logout(request)
    return redirect('home')


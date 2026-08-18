
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from blogs.models import Category, Blog
from aboutUs.models import About
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


def home(request):
    categories = Category.objects.all()
    featured_post = Blog.objects.filter(is_featured=True, status='Published').order_by('updated_at')
    recent_post = Blog.objects.filter(is_featured=False, status='Published').order_by('updated_at')

    try:
        about = About.objects.get()
    except:
        about = None

    context = {
        'categories': categories,
        'featured_post': featured_post,
        'recent_post': recent_post,
        'about': about,
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


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
        'categories': Category.objects.all(),
    }
    return render(request, 'login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistrationForm()
    context = {
        'form': form,
        'categories': Category.objects.all(),
    }
    return render(request, 'register.html', context)


def dashboard(request):
    return redirect('home')


def logout_view(request):
    logout(request)
    return redirect('home')


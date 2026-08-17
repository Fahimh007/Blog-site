from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import Category, Blog
from django.db.models import Q


def category_posts(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    posts = Blog.objects.filter(status='Published', category=category)

    if not posts.exists():
        raise Http404("No posts found for this category.")

    context = {
        'posts': posts,
        'category': category,
        'category_id': category_id,
    }
    return render(request, 'category_posts.html', context)
    
def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug, status='Published')
    context = {
        'single_blog': blog,
    }
    return render(request, 'blog_detail.html', context)

def search(request):
    keyword = request.GET.get('keyword')
    
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='Published')
  
    context = {
        'blogs': blogs,
        'keyword': keyword,
    }
    return render(request, 'search.html', context)
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import Category, Blog


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
    
   
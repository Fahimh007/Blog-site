from django.urls import path
from . import views

urlpatterns = [
    path('posts-by-category/<int:category_id>/', views.category_posts, name='posts_by_category'),
]
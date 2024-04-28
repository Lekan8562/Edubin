from django.urls import path

from .views import post_detail,posts,category_posts



app_name = 'blog'

urlpatterns = [
        path('posts/',posts,name="posts"),
        path('post/<slug:post_slug>/',post_detail,name="post_detail"),
        path('<slug:category_slug>/posts/',category_posts,name='category_posts')
        
]
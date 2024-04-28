from django.shortcuts import render,get_object_or_404
from django.db.models import Count

from course.models import Category

from .models import Post


# Create your views here.


def posts(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    context = {'posts':posts,'categories':categories}
    return render(request,'blog.html',context)


def post_detail(request,post_slug):
    post = get_object_or_404(Post,slug__iexact = post_slug)
    related_posts = Post.objects.filter(category=post.category).exclude(id=post.id)
    related_posts = Post.objects.annotate(same_categories=Count('category')).order_by('-same_categories','-created')[:4]
    context = {'post':post,'related_posts':related_posts}
    return render(request,'posts/post_detail.html',context)


def category_posts(request,category_slug):
    category = get_object_or_404(Category, slug__iexact = category_slug)
    posts = category.category_posts.all()
    categories = Category.objects.all()
    context = {'posts':posts,'categories':categories,'category':category}
    return render(request,'category_posts.html',context)
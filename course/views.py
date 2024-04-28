from django.shortcuts import render,get_object_or_404
from .models import Event,Course,Category,Teacher
from django.db.models import Count,Q
from blog.models import Post
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from accounts.models import CustomUser
# Create your views here.

def home(request):
    events = Event.objects.all()
    posts = Post.objects.all()
    post_1 = posts[:1]
    courses = Course.objects.all()
    categories = Category.objects.all()
    teachers = CustomUser.objects.filter(role='teacher')
    context = {'events':events,'courses':courses,'posts':posts,'post_1':post_1,'categories':categories,'teachers':teachers}
    return render(request,"course/home.html",context)

def search_courses(request):
    query = request.GET.get('q','')
    courses = Course.objects.filter(
        Q(title__icontains=query)
    ).distinct()
    context = {'courses':courses,'query':query}
    return render(request,'course/search_courses.html',context)

def courses(request):
    course_list = Course.objects.all()
    paginator = Paginator(course_list, 10)
    page_number = request.GET.get('page')
    
    try:
        courses = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        courses = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        courses = paginator.page(paginator.num_pages)
    
    return render(request, 'course/courses.html', {'courses': courses,'course_list':course_list})


def course_detail(request,course_slug):
    course = get_object_or_404(Course, slug__iexact=course_slug)
    similar_courses = Course.objects.filter(category=course.category).exclude(id=course.id)
    similar_courses = similar_courses.annotate(same_categories=Count('category')).order_by('-same_categories','-created')[:4]
    context = {'course':course,'similar_courses':similar_courses}
    return render(request,'course/course_detail.html',context)


def events(request):
    event_list = Event.objects.all()
    paginator = Paginator(event_list,10)
    page_number = request.GET.get('page')
    try:
        events = paginator.page(page_number)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = pagnator.page(paginator.num_pages)
    
    return render(request,'events/events.html',{'events':events})

def event_detail(request,event_slug):
    event = get_object_or_404(Event, slug__iexact=event_slug)
    context = {'event':event}
    return render(request,'events/event_detail.html',context)

def category_courses(request,category_slug):
    category = get_object_or_404(Category, slug__iexact=category_slug)
    courses = category.category_courses.all()
    context = {'courses':courses,'category':category}
    return render(request,'course/category_courses.html',context)
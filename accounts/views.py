from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate

from course.models import Course,Event,Teacher,Category
from blog.models import Post
from library.models import Book

from .forms import LoginForm
from .models import School,Department,CustomUser

# Create your views here.

def about(request):
    context = {}
    return render(request,'accounts/about.html',context)


@login_required
def user_home(request):
    user = request.user
    user_school = user.school
    user_department = user.department
    schools = School.objects.all()
    events = Event.objects.filter(school = user_school)
    posts = Post.objects.all()
    post_1 = posts[:1]
    books = Book.objects.filter(
        related_schools = user_school,
        related_departments = user_department
     )
    teachers = CustomUser.objects.filter(role='teacher')
    categories = Category.objects.all()
    context = {'events':events,
               'schools':schools,
               'teachers':teachers,
               'posts':posts,
               'post_1':post_1,
               'books':books,
               'categories':categories
               }
    return render(request,'accounts/home.html',context)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username = cd['username'],
                                password = cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('accounts:user_home')
                else:
                    return HttpResponse('Disabled User')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
    return render(request,'registration/login.html',{'form':form})

def user_logout(request):
    logout(request)
    return redirect('course:home')
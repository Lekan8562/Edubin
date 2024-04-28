from django.shortcuts import render,get_object_or_404

from .models import Book

# Create your views here.

def books(request):
    user = request.user
    user_school = user.school
    user_department = user.department
    books = Book.objects.filter(related_schools = user_school, related_departments = user_department)
    context = {'books':books}
    return render(request,'books.html',context)

def book_detail(request,book_slug):
    book = get_object_or_404(Book,slug__iexact = book_slug)
    context = {'book':book}
    return render(request,'library/book_detail.html',context)
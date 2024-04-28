from django.urls import path
from .views import books,book_detail

app_name = 'library'

urlpatterns = [
    path('books/',books,name='books'),
    path('books/<slug:book_slug>/',book_detail,name='book_detail')
]
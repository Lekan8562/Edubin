from django.urls import path
from .views import user_login,user_home,user_logout,about
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
        path('login/',user_login,name='login'),
        path('logout/',user_logout,name='logout_user'),
        path('home/',user_home,name='user_home'),
        path('about_us/',about,name='about')
]
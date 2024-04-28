from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from blog.views import *

from . import views

app_name = 'course'

urlpatterns = [
        path('',views.home,name="home"),
        path('courses/all/',views.courses,name="courses"),
        path('course/<slug:course_slug>/',views.course_detail,name='course_detail'),

        path('courses/search/',views.search_courses,name='search'),
        
        path('post/<slug:post_slug>/',post_detail,name="post_detail"),
        
        path('events/all/',views.events,name='events'),
        path('event/<slug:event_slug>/',views.event_detail,name='event_detail'),
        path('<slug:category_slug>/courses/',views.category_courses,name="category_courses")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
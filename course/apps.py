from django.apps import AppConfig


class CourseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'course'
    def ready(self):
        # Import the models after the application registry is ready
        from .models import Course

from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    courses = models.ManyToManyField('course.Course',related_name='course_schools')
    
    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    courses = models.ManyToManyField('course.Course',related_name='course_departments')
    
    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    ROLE_CHOICES = {
        ('student', 'Student'),
        ('teacher','Teacher'),
    }
    profile_picture = models.ImageField(upload_to='profile_pictures/',blank=True,null=True)
    school = models.ForeignKey(School,related_name='school_users',on_delete=models.CASCADE,null=True)
    department = models.ForeignKey(Department,related_name='department_users',on_delete=models.CASCADE,null=True)
    bio = models.TextField(blank=True)
    role = models.CharField(max_length=20,choices=ROLE_CHOICES)
    groups = models.ManyToManyField(
            'auth.Group',
            related_name='custom_users',
            blank=True,
            verbose_name='groups',
            help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_users',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )
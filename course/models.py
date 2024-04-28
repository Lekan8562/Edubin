from django.db import models
#from accounts.models import Teacher,Student
from accounts.models import School,Department
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from bs4 import BeautifulSoup
from django.urls import reverse
from accounts.models import CustomUser
# Create your models here.



class Teacher(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name='user_teacher',null=True)

    niche = models.CharField(max_length=50)
    about = models.TextField()
    def __str__(self):
        return f'{self.user} - {self.niche}'
    
class Student(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name='user_student',null=True)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='student/image')
    bio = models.TextField()
    def __str__(self):
        return self.name




class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('course:category_courses',kwargs={'category_slug':self.slug})

    def __str__(self):
        return self.name
    
class Event(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    image = models.ImageField(upload_to='event/images')
    created = models.DateTimeField(auto_now_add=True,null=True)
    starting_time = models.DateTimeField(null=True)
    finish_time = models.DateTimeField(null=True)
    school = models.ForeignKey(School,related_name='school_events',on_delete=models.CASCADE,null=True)
    address = models.CharField(max_length=150)
    description = models.TextField()
    class Meta:
        ordering = ['created']
    def get_absolute_url(self):
        return reverse('course:event_detail',kwargs={'event_slug':self.slug})
    def __str__(self):
        return self.name


    

class Curriculum(models.Model):
    course = models.ForeignKey('Course',related_name='course_topics',on_delete=models.CASCADE)
    lecture_number = models.FloatField(null=True)
    title = models.CharField(max_length=150)
    body = FroalaField()
    video = models.FileField(upload_to='courses/files',null=True,blank=True)
    duration = models.TimeField(null=True)
    class Meta:
        ordering = ['lecture_number']
    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    cover_image = models.ImageField(upload_to='course/cover',null=True)
    description = FroalaField()
    who_needs_course = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category,related_name='category_courses',on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher,related_name='teacher_courses',on_delete=models.CASCADE)
    students = models.ManyToManyField(Student,related_name='student_courses')
    school = models.ManyToManyField(School,related_name='school_courses',blank=True)
    department = models.ManyToManyField(Department,related_name='department_courses',blank=True)
    paid = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['created']
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('course:course_detail',kwargs={'course_slug':self.slug})
    def get_cover_image_url(self):
        soup = BeautifulSoup(self.description, 'html.parser')
        img_tag = soup.find('img')
        if img_tag and img_tag.has_attr('src'):
            return img_tag['src']
        return None
#-----------------QUIZES----------------

class Quiz(models.Model):
    topic = models.ForeignKey(Curriculum,related_name='course_quizes',on_delete=models.CASCADE,null=True)
    question_number = models.PositiveIntegerField()
    question = models.TextField()
    def __str__(self):
        return f'{self.question} -- in -- {self.course.title}'

class Option(models.Model):
    question = models.ForeignKey(Quiz,related_name='quiz_options',on_delete=models.CASCADE)
    lettering = models.CharField(max_length=1)
    answer = models.TextField()
    corrrect = models.BooleanField(default=False)
    def __str__(self):
        return f'option {self.lettering} -- in -- {self.question} {self.answer}'
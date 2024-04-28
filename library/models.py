from django.db import models
from accounts.models import School,Department
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    image = models.ImageField(upload_to='books/images',null=True,blank=True) 
    author = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    related_schools = models.ManyToManyField(School,related_name='course_books',blank=True)
    related_departments = models.ManyToManyField(Department,related_name='department_books',blank=True)

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('library:book_detail', kwargs={slug:self.slug})

    def __str__(self):
        return self.name
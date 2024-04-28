from django.db import models
from course.models import Category
from froala_editor.fields import FroalaField
from accounts.models import CustomUser
from django.urls import reverse

class Tag(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)
    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name



class Post(models.Model):
    category = models.ForeignKey(Category,related_name='category_posts',on_delete=models.CASCADE,null=True)
    tags = models.ManyToManyField(Tag,related_name='tag_posts')
    author =  models.ForeignKey(CustomUser,related_name='author_posts',on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to='post/cover',null=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    body = FroalaField()
    class Meta:
        ordering = ['title','-created']
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:post_detail',kwargs={'post_slug':self.slug})



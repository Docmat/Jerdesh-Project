from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime
from django.urls import reverse



class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'


    def __str__(self):
        return self.name


     
class Advert(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(get_user_model(), on_delete = models.CASCADE,)
    text = models.TextField()
    img = models.ImageField(upload_to='advert/photos',default='media/default.jpg')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.title
        

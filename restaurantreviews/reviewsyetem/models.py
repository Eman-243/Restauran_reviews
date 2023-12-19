from django.urls import reverse
import datetime
from django.db import models
from djongo import models
import uuid



from django.contrib.auth.models import User

class Restaurant(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    price = models.CharField(max_length=10)  
    img = models.CharField(max_length=100)  
    
    def __str__(self):
        return self.title
    
 
 
class Comment1(models.Model):
    title = models.CharField(max_length=100)  
    description = models.CharField(max_length=500)
    restaurant_id = models.CharField(max_length=20)
    author=models.ForeignKey(User,on_delete =models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
    def is_author(self, user):
     return self.author == user

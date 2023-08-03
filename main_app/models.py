from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

class Dish(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'food_id': self.id})


class Comment(models.Model):
    dish_id = models.ForeignKey(Dish,on_delete=models.CASCADE,related_name='comments')    
    city_name = models.CharField(max_length=80, verbose_name='City', default='')    
    restaurant_name = models.CharField(max_length=100, verbose_name='Restaurant Name', default='')
    body = models.TextField()    
    created_on = models.DateTimeField(auto_now_add=True)    
        
    
    class Meta:        
        ordering = ['created_on']    
    
    
    def __str__(self):        
        return 'Comment {} by {}'.format(self.body, self.dish_id)

    

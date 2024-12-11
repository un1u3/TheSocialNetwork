from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images/')
    datetime = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.user
    
    
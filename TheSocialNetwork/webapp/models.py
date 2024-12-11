from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    slug = models.SlugField(unique=True ,blank=True) # blank = true for empty initilization
    image = models.ImageField(upload_to='images/',blank=True)
    datetime = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=50,blank=True)
    
    def save(self, *args, **kwargs):
        # Auto-generate slug if it doesn't exist
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    
    def __str__(self):
        return self.title
    
    
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True)  # Allows blank initialization
    image = models.ImageField(upload_to='images/', blank=True)
    datetime = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=50, blank=True)
    
    def save(self, *args, **kwargs):
        # Generate unique slug
        if not self.slug:
            base_slug = slugify(self.title)
            unique_slug = base_slug
            counter = 1

            while Post.objects.filter(slug=unique_slug).exists():
                unique_slug = f'{base_slug}-{counter}'
                counter += 1

            self.slug = unique_slug
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title

    
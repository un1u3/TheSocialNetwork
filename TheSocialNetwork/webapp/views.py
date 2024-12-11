from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'webapp/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context
    
    

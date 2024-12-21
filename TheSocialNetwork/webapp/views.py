from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .forms import PostForm
from django.urls import reverse_lazy



# Create your views here.

class HomeView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'webapp/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context
    
    
class PostCreateView(LoginRequiredMixin,CreateView):
    model = 'Post'
    template_name =  'webapp/createpost.html'
    form_class  = PostForm
    success_url = reverse_lazy('home')  
    
    def form_valid(self, form):
        form.instance.user = self.request.user  # Set the user before saving
        return super().form_valid(form)
    

    

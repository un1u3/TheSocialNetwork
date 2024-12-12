# views.py
from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login  
from django.contrib.auth import logout
from django.views.generic import View
from django.shortcuts import redirect
from django.contrib import messages

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('home')  # Redirect after successful registration

    def form_valid(self, form):
        user = form.save()  # Save the user
        login(self.request, user)  # Log the user in immediately after registration
        return super().form_valid(form)


from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'user/login.html'

    def get_success_url(self):
        return '/'




class CustomLogoutView(View):
    """
    A view that handles user logout, clears the session, 
    and redirects to the home page.
    """
    def get(self, request):
        logout(request)
        messages.success(request, "You have been successfully logged out.")
        return redirect('home')  
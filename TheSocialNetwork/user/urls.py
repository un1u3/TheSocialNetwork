from django.urls import path 
import user.views as auth_views




urlpatterns = [
    path('register/',auth_views.RegisterView.as_view(),name='register'),
    path('login/', auth_views.CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.CustomLogoutView.as_view(), name='logout'),
   
]

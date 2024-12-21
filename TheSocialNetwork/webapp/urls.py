from  django.urls import path 
from . import views 

urlpatterns = [
    path('',views.HomeView.as_view(), name='home'),
    path('upload-post/',views.PostCreateView.as_view(), name='upload'),
]

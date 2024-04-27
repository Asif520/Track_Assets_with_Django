from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginUser, name ='login'),
    path('logout/',views.logoutUser, name ='logout'),
    path('register/',views.registerUser, name ='register'),
    
    path('',views.home, name ='home'),
    path('company/<str:pk>/',views.company, name ='company'),
    


]
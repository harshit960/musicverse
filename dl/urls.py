from django.urls import path
from .views import signup_page,handlelogin,handlelogout
urlpatterns = [
    
    path('signup', signup_page , name='Signup'),
    path('login', handlelogin , name='login'),
    path('logout', handlelogout , name='logout'),
    
]


    
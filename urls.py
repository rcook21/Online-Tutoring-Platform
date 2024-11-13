from django.urls import path
from .views import home,login_page, register_page,course,join

urlpatterns = [
    path('', home ,name='home'),  # Home page or login page
    path('login/', login_page, name='login'),  # Handle login requests
    path('register/',register_page, name='register'),  # Course page
    path('course/', course, name= 'course'),
    path('join/',join, name='join')

]


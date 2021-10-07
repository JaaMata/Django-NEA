from django.contrib import admin
from django.contrib.auth import logout
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create/student', CreateStudentView.as_view(), name='create_student'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('signup', SignUp.as_view(), name='signup')






]

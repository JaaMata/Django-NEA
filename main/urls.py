from django.contrib import admin
from django.contrib.auth import logout
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('create/student', CreateStudent.as_view(), name='create_student'),
    path('login', Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout')





]

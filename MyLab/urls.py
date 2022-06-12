from django.contrib import admin
from django.urls import path
from MyLab import views

urlpatterns = [
    path("", views.Home, name='Home'),
    path("Student", views.Student, name='Student'),
    path("Staff", views.Staff, name='Staff'),
    path("Courses", views.Courses, name='Courses'),
    path("Subjects", views.Subjects, name='Subjects'),
]


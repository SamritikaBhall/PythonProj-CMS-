from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Course)
admin.site.register(Subjects)

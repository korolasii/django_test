from django.contrib import admin
from .models import Student, Course, Company, Department, Position
from django.contrib import admin

admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Company)

from django.db import models
from .course import Course

class Student(models.Model):
    class Meta:
        db_table = "it_students"

    first_name = models.TextField(null=False)
    last_name = models.TextField(null=False)
    completed_lessons = models.IntegerField()
    birth_date = models.DateField(null=True)
    avatar = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course, to_field='name', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, null=True)  




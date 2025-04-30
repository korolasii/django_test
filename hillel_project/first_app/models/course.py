from django.db import models


class Course(models.Model):
    name = models.TextField(unique=True)
    description = models.TextField()
    learning_plan = models.TextField()


from django.db import models
from .department import Department

class Position(models.Model):
    title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    department = models.ForeignKey(Department, related_name='position', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.department.name})"
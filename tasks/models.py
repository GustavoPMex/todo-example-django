from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class tasksModel(models.Model):
    description = models.CharField(max_length=200,null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True, null=False, blank=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.description

    class meta:
        verbose_name = 'task'
        verbose_name_plural = 'tasks'
        ordering = ['-date']

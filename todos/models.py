from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Task(models.Model):
    auther = models.ForeignKey(User, related_name='task_user', on_delete=models.CASCADE, null=True, blank=True)
    task = models.CharField(max_length=100)
    task_text = models.TextField(max_length=1000)
    date = models.DateTimeField(default=timezone.now)
    complate = models.BooleanField(default=False)

    def __str__(self):
        return self.task

    class Meta:
        order_with_respect_to = 'auther'
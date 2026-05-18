from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', 'До виконання'),
        ('in_progress', 'В процесі'),
        ('review', 'На перевірці'),
        ('done', 'Виконано'),
    ]

    PRIORITY_CHOICES = [
        ('low', 'Низький'),
        ('medium', 'Середній'),
        ('high', 'Високий'),
        ('urgent', 'Терміновий'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='low')

    assignee = models.CharField(max_length=100)

    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    task = models.ForeignKey(Task,on_delete=models.CASCADE,related_name='comments')

    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments')

    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username}: {self.text[:20]}"
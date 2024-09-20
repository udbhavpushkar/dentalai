from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ('queued', 'Queued'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='queued')
    task_id = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title

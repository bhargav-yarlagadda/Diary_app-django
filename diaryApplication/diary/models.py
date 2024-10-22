from django.db import models
from django.utils import timezone

class Entry(models.Model):
    header = models.CharField(max_length=100)
    entry = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)  # Set a default value here

    def __str__(self):
        return self.header

from django.db import models

class ToDo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    time = models.TimeField()

    def __str__(self):
        return self.title
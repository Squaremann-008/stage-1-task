from django.db import models

# Create your models here.
class student(models.Model):
    slackUsername = models.CharField(max_length=100)
    backend = models.BooleanField(default=True)
    age = models.IntegerField()
    bio = models.TextField(max_length=100)
    
    def __str__(self):
        return self.slackUsername
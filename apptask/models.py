from django.db import models

# Create your models here.
class contact(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    phone_number=models.CharField(max_length=10)
    Message=models.TextField()

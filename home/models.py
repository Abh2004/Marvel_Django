from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.EmailField(max_length=122)
    subject=models.CharField(max_length=500)
    message=models.CharField(max_length=600)
    date=models.DateField()


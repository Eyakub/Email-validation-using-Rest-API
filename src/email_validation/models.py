from django.db import models

# Create your models here.
class EmailValidation(models.Model):
    email = models.EmailField(max_length=255)
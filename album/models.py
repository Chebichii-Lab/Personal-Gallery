from django.db import models

# Create your models here.

# Image class
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)
    description = models.TextField()
    # category = models.ForeignKey()
    # location = models.ForeignKey()

# Category class 
class Category(models.Model):
    name = models.CharField(max_length=100)




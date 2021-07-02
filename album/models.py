from django.db import models

# Create your models here.

# Category class 
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

# Location class
class Location(models.Model):
    name = models.CharField(max_length=100)

    @classmethod
    def get_locations(cls):
        locations = Location.objects.all()
        return locations

    def __str__(self):
        return self.name

    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()


# Image class
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey( Category, on_delete=models.CASCADE , default='0')
    location = models.ForeignKey( Location, on_delete=models.CASCADE , default='0')


    


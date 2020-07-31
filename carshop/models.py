
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class car(models.Model):
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    milage = models.IntegerField()
    emissions = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    new = models.BooleanField()
    sold = models.BooleanField()
    soldDate = models.DateField(null=True, blank =True)
    postDate = models.DateField()
    Main_Image = models.ImageField(default='media/default.jpg')
    Side_Image = models.ImageField(default='media/default.jpg')
    Back_Image = models.ImageField(default='media/default.jpg')
    Front_Image = models.ImageField(default='media/default.jpg')
    Interior_Image = models.ImageField(default='media/default.jpg')
    Other_Image = models.ImageField(default='media/default.jpg')

    def __str__(self):
        return f"{self.make} {self.model} {self.year} -> £{self.cost}"

class Message(models.Model):
    text = models.TextField()
    email = models.CharField(max_length=255)
    responded = models.BooleanField(default=False)
    def __str__(self):
        return self.email

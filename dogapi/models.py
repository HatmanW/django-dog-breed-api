from django.db import models

# Create your models here.

class Dogs(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    color = models.CharField(max_length=50)
    favorite_food = models.CharField(max_length=50)
    favoritetoys = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Breeds(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    friendliness = models.IntegerField()
    trainability = models.IntegerField()
    sheddingamount = models.IntegerField()
    exerciseneeds = models.IntegerField()

    







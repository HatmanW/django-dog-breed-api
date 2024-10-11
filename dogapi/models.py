from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator #interesting import

# Create your models here.

class Dog(models.Model):
    '''appearently if these aren't named single '''
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    color = models.CharField(max_length=50)
    favorite_food = models.CharField(max_length=50)
    favoritetoys = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Breed(models.Model):
    '''never really done these before so this is a cool test out.
    https: // docs.djangoproject.com / en / 5.1 / ref / models / fields /  # choices
    and https://docs.djangoproject.com/en/5.1/ref/validators/#minvaluevalidator '''

    SIZE_OPTIONS = [
        ('Tiny', 'Tiny'),
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    ]

    name = models.CharField(max_length=100)
    size = models.CharField(max_length=50, choices=SIZE_OPTIONS)
    friendliness = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    trainability = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    sheddingamount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    exerciseneeds = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.name







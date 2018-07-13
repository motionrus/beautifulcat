from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Cat(models.Model):
    HEAR_CHOICES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', "Female")
    )
    name = models.TextField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(20)]
    )

    color = models.TextField()
    weight = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(50)]
    )
    hair = models.CharField(max_length=1, choices=HEAR_CHOICES)

    def __str__(self):
        return self.name


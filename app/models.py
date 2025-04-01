from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

# Restaurat
# User
# Rating

def custom_validation(value):
    if not value.startwith('a'):
        raise ValidationError('Name should start with "a"')

class Restaurant(models.Model):
    class TypeChoices(models.TextChoices):
        INDIAN = 'IN', 'Indian'
        CHINESE = 'CH', 'Chinese'
        ITALIAN = 'IT', 'Italian'
        GREEK = 'GR', 'Greek'

    name = models.CharField(max_length=100, validators = [custom_validation])
    website = models.URLField(default = '')
    date_opened = models.DateField()
    latitude = models.FloatField(validators = [MinValueValidator(-90), MaxValueValidator(90)])
    longitude = models.FloatField(validators = [MinValueValidator(-180), MaxValueValidator(180)])
    restaurant_type = models.CharField(max_length=2, choices = TypeChoices.choices)

    def __str__(self):
        return self.name


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='ratings')
    ratings = models.PositiveSmallIntegerField(validators = [MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f'Rating : {self.ratings}'
    
class Sale(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True, related_name='sales')
    income = models.DecimalField(max_digits=8, decimal_places=2)
    datetime = models.DateTimeField()

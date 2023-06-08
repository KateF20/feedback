from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Review(models.Model):
    user_name = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])

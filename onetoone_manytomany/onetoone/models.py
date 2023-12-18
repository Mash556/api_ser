from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=100)
    population = models.IntegerField()

class Capital(models.Model):
    name = models.CharField(max_length=100)
    country = models.OneToOneField(
        Country, 
        on_delete=models.CASCADE,
        related_name='human'  # обратная связь
        )
    
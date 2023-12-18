from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Application(models.Model):
    reviews = models.IntegerField()
    user = models.ManyToManyField(
        User,
        related_name='application'
        )
    def __str__(self):
        return self.reviews



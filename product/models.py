from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(null=True)
    expiried_date = models.DateField(null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.title} -> {self.pk}'
    
    class Meta:
        verbose_name = 'Продукты'



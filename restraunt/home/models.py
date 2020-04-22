from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Food(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Item(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=30)
    item_price = models.IntegerField()
    item_qty = models.IntegerField(default=0, choices=((0,0), (1,1), (2,2), (3,3), (4,4), (5,5)))

    def __str__(self):
        return self.item_name









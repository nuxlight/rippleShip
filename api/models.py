from django.db import models

class Grid(models.Model):
    width = models.IntegerField()
    height = models.IntegerField()

class Party(models.Model):
    party_number = models.CharField(max_length=5)
    grid = models.ForeignKey(Grid, on_delete=models.CASCADE)

class ShipType(models.Model):
    name = models.CharField(max_length=25)

class Ship(models.Model):
    party = models.ForeignKey(Party,on_delete=models.CASCADE)
    ship_type = models.ForeignKey(ShipType, on_delete=models.CASCADE)
    is_destroy = models.BooleanField(default=False)

class Position(models.Model):
    ship = models.ForeignKey(Ship, on_delete=models.CASCADE)
    abs = models.IntegerField()
    ord = models.IntegerField()
    is_destroy = models.BooleanField(default=False)
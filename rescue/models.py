# rescue/models.py
from django.db import models

class Victim(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    location_lat = models.FloatField()
    location_lon = models.FloatField()
    need = models.TextField()

    def __str__(self):
        return self.name


class Rescuer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    location_lat = models.FloatField()
    location_lon = models.FloatField()
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Guest(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    victim = models.ForeignKey(Victim, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return self.name

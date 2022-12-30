from django.db import models

class Familiars(models.Model):
    name = models.CharField(max_length=100)
    edad = models.IntegerField()
    genero = models.BooleanField()

class Profession(models.Model):
    name = models.CharField(max_length=50, unique=True)

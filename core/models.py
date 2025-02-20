from django.db import models

# Create your models here.
class Agency(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)
    founding_year = models.IntegerField()
    budget = models.IntegerField()

    def __str__(self):
        return self.name

class Astronaut(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    birth_date = models.DateField()
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, related_name='astronauts')

    def __str__(self):
        return self.name


class Planet(models.Model):
    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=100)
    discovery_date = models.DateField()

    def __str__(self):
        return self.name

class Spacecraft(models.Model):
    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=100)
    launch_date = models.DateField()
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, related_name='spacecrafts')
    visited_planets = models.ManyToManyField(Planet, related_name='spacecrafts', blank=True)

    def __str__(self):
        return self.name


class Mission(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    launch_date = models.DateField()
    duration_days = models.IntegerField()
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, related_name='missions')
    spacecrafts = models.ManyToManyField(Spacecraft, related_name='missions')
    planets = models.ManyToManyField(Planet, related_name='missions')

    def __str__(self):
        return self.name




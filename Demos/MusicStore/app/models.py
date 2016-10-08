"""
Definition of models.
"""

from django.db import models
from django import forms

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=50)
    year_formed = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist)

    def __str__(self):
        return self.name
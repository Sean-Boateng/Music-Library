from django.db import models
import datetime

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    release_date = models.DateField(auto_now_add=True)
    genre = models.CharField(max_length=255)
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import Permission, User

# Create your models here.


class Album(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    artist = models.CharField(max_length=250)
    albumTitle = models.CharField(max_length=500)
    gener = models.CharField(max_length=100)
    albumLogo = models.FileField()
    isFavorite = models.BooleanField(default=False)

    def __str__(self):
        return self.artist+' - '+self.albumTitle+' - '+self.gener


class Song(models.Model):

    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    fileType = models.FileField(default='')
    songTitle = models.CharField(max_length=250)
    isFavorite = models.BooleanField(default=False)

    def __str__(self):
        return self.album.albumTitle+' - '+self.songTitle

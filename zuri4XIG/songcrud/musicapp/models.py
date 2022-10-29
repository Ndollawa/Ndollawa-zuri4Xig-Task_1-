from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField(max_length=3)
    


class Song(models.Model):
    title = models.CharField(max_length=255)
    date_released = models.DateTimeField(max_length=255)
    likes = models.IntegerField(max_length=255)
    artiste_id = models.ForeignKey(Artiste)


class Lyrics(models.Model):
    content = models.CharField(max_length=1000,)
    song_id = models.ForeignKey(Song)

from django.db import models

# Create your models here.


class Singer(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Album(models.Model):
    album_name = models.CharField(max_length=50)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)
    create_date = models.DateField()

    def __str__(self):
        return str(self.album_name) + str(self.create_date) + str(self.singer)


class Song(models.Model):
    song_name = models.CharField(max_length=100)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.song_name) + str(self.album)


class Playlist(models.Model):
    playlist_name = models.CharField(max_length=100)
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.playlist_name




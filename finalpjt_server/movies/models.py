from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    genre_number = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)

class Movie(models.Model):
    movie_like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="movie_like", blank=True)
    genres = models.ManyToManyField(Genre, through='Movie_Genre')
    movie_id = models.IntegerField()
    title = models.CharField(max_length=150)
    poster_path = models.CharField(max_length=1000)
    overview = models.TextField()
    release_date = models.DateField()

class Movie_Genre(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, to_field='genre_number')



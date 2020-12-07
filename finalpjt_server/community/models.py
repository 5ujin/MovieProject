from django.db import models
from django.conf import settings
from movies.models import Movie

# Create your models here.
class Review(models.Model):
    user = models.CharField(max_length=50)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_review", blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movies_reviews')
    review_title = models.CharField(max_length=200)
    review_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rank = models.IntegerField()
    genre = models.IntegerField()
    poster_path = models.CharField(max_length=1000)
    movie_title = models.CharField(max_length=150)
    
class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    user = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


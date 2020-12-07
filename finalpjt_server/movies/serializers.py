from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'movie_like_users', 'genres', 'movie_id', 'title', 'poster_path', 'overview', 'release_date', 'movies_reviews')
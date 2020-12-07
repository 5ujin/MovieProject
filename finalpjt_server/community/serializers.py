from django.db.models import fields
from django.db.models.fields import IntegerField
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from .models import Review, Comment

class CommentSerializer(serializers.ModelSerializer):


    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['user', 'review']


class ReviewSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = ('id','user', 'like_users', 'movie', 'review_title', 'review_content', 'created_at', 'updated_at', 'rank', 'comments', 'genre', 'poster_path','movie_title')
        read_only_fields = ['user', 'comments', 'like_users', 'genre', 'poster_path', 'movie_title']

        

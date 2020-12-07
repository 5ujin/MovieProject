from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import ReviewSerializer, CommentSerializer

from .models import Comment, Review
from movies.models import Movie, Genre, Movie_Genre
# Create your views here.

@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_list_create(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            movie = Movie.objects.get(pk=request.data['movie'])
            reviews_genre = Movie_Genre.objects.filter(movie_id=request.data['movie'])[0].genre_id
            serializer.save(user=request.user.username, genre=reviews_genre, poster_path=movie.poster_path, movie_title=movie.title)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_detail_update_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comments = Comment.objects.filter(review=review_pk).order_by('-id')
    print(review)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        if review.like_users.filter(pk=request.user.pk).exists():
            review.like_users.remove(request.user)
        else:
            review.like_users.add(request.user)
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'PUT':
        if request.user.username == review.user:
            serializer = ReviewSerializer(review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(movie=review.movie)
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    else:
        if request.user.username == review.user:
            review.delete()
            return Response({'id' : review_pk}, status=status.HTTP_202_ACCEPTED)

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_create(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(review=review, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user.username == comment.user:
        comment.delete()
        return Response({'id': comment_pk}, status=status.HTTP_202_ACCEPTED)
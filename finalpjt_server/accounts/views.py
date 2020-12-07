from django.http import request
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import User
from .serializers import UserSerializer

# Create your views here.
@api_view(['POST'])
def signup(request):
    password = request.data.get('password')
    password_confirm = request.data.get('passwordConfirm')
    
    if password != password_confirm:
        return Response({'error' : '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def profile_follow(request, username):
    me = request.user
    person = get_object_or_404(User, username=username)
    if request.method == 'GET':
        serializer = UserSerializer(person)
        return Response(serializer.data)
    else:
        if me != person:
            if person.followers.filter(username=me).exists():
                person.followers.remove(me)
            else:
                person.followers.add(me)
        serializer = UserSerializer(person)
        return Response(serializer.data)
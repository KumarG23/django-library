from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .models import *
from .serializers import *

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):
    user = request.user
    profile = user.profile
    serialized_profile = ProfileSerializer(profile)
    return Response(serialized_profile.data)

@api_view(['POST'])
@permission_classes([])
def create_user(request):
    user = User.objects.create(
        username = request.data['username'],
    )
    user.set_password(request.data['password'])
    user.save()
    profile = Profile.objects.create(
        user = user,
        first_name = request.data['first_name'],
        last_name = request.data['last_name']
    )
    profile.save()
    profile_serialized = ProfileSerializer(profile)
    return Response(profile_serialized.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_books(request):
    user = request.user
    try:
        profile = Profile.objects.get(user=user)
        books = Book.objects.filter(profile=profile)
        serialized_book = BookSerializer(books, many=True)
        return Response(serialized_book.data)
    except Profile.DoesNotExist:
        return Response({'Error': 'Profile not found'}, status=404)

    # books = Book.objects.all()
    # serialized_book = BookSerializer(books, many=True)
    # return Response(serialized_book.data)
    # if serialized_book.data:
    # print('HELLO!: ', serialized_book)
    # return Response({'message': 'HOWDY!'}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_book(request):
    user = request.user
    profile = user.profile
    author, created = Author.objects.get_or_create(
        name = request.data['author']
    )
    author.save()
    genre, created = Genre.objects.get_or_create(
        name = request.data['genre']
    )
    genre.save()
    book = Book.objects.create(
        title = request.data['title'],
        author = author,
        genre = genre,
        profile = profile
    )
    book.save()
    serialized_book = BookSerializer(book, data=request.data)
    if serialized_book.is_valid():
        return Response(serialized_book.data)
    return Response(serialized_book.errors)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_book(request, pk):
    user = request.user
    profile = user.profile
    try:
        book = Book.objects.get(pk=pk, profile=profile)
    except Book.DoesNotExist:
        return Response({'error': 'Book not found'})
    
    serialized_book = BookSerializer(book, data=request.data)
    if serialized_book.is_valid():
        serialized_book.save()
        return Response(serialized_book.data)
    return Response(serialized_book.errors)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response({'error': 'Book not found'})
    
    book.delete()
    return Response(status=204)
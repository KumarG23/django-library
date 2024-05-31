from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.name')
    genre = serializers.CharField(source='genre.name')
    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        author_name = validated_data.pop('author')['name']
        genre_name = validated_data.pop('genre')['name']

        author, created = Author.objects.get_or_create(name=author_name)

        genre, created = Genre.objects.get_or_create(name=genre_name)

        book = Book.objects.create(author=author, genre=genre, **validated_data)

        return book



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
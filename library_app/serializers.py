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
    author = serializers.CharField(source='author.name', required=False, read_only=True)
    genre = serializers.CharField(source='genre.name', required=False, read_only=True)
    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        author_name = validated_data.pop('author', None)
        genre_name = validated_data.pop('genre', None)

        author = Author.objects.get_or_create(name=author_name)[0] if author_name else None

        genre = Genre.objects.get_or_create(name=genre_name)[0] if genre_name else None

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
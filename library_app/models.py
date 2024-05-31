from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.TextField(default='')
    last_name = models.TextField(default='')

    def __str__(self):
        return self.user.username
    
class Book(models.Model):
    title = models.CharField(max_length=100, default='')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, default='', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField()

    def __str__(self):
        return f'{self.user.username} - {self.book.title}'




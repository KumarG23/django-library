from django.contrib import admin
from library_app.models import *


class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)


class BookAdmin(admin.ModelAdmin):
    pass

admin.site.register(Book, BookAdmin)

class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Author, AuthorAdmin)

class GenreAdmin(admin.ModelAdmin):
    pass

admin.site.register(Genre, GenreAdmin)

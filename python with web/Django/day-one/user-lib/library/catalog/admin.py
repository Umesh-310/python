from django.contrib import admin

from .models import Language, Book, Author, BookInce, Genre
# Register your models here.

admin.site.register(Language)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookInce)
admin.site.register(Genre)
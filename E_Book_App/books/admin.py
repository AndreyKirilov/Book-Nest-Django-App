from django.contrib import admin

from E_Book_App.books.models import Author, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'bio']
    list_filter = ['name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'publication_date']
    list_filter = ['title']
    ordering = ['publication_date']

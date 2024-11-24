from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author_books')
    description = models.TextField(blank=True, null=True)
    publication_date = models.DateField()
    cover_image = models.ImageField(upload_to='book_images', blank=True, null=True)

    def __str__(self):
        return self.title

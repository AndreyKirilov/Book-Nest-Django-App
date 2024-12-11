from django.contrib.auth import get_user_model
from django.db import models
from E_Book_App.books.models import Book


AppUserModel = get_user_model()


class Favourites(models.Model):
    user = models.ForeignKey(AppUserModel, on_delete=models.CASCADE, related_name='user_favourites')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'book')

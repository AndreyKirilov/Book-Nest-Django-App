from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinLengthValidator

from E_Book_App.books.models import Book


AppUserModel = get_user_model()


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_reviews')
    user = models.ForeignKey(AppUserModel, on_delete=models.CASCADE, related_name='user_reviews')
    body = models.TextField(max_length=300, null=False, blank=False,
                            validators=[MinLengthValidator(5, message="Comment must be at least 5 chars long!")])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"A review for {self.book.title}"

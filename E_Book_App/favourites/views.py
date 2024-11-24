from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView

from E_Book_App.books.models import Book
from .models import Favourites


def add_to_wishlist_view(request, book_id):
    book = Book.objects.get(pk=book_id)
    Favourites.objects.create(user=request.user, book=book)
    return redirect('favourites')


class FavouritesView(LoginRequiredMixin, ListView):
    model = Favourites
    template_name = 'favourites/favourite_books.html'
    context_object_name = 'favourite_books'

    def get_queryset(self):
        return Favourites.objects.filter(user=self.request.user)


def remove_from_wishlist_view(request, book_id):
    book = Book.objects.get(pk=book_id)
    Favourites.objects.filter(book=book).delete()
    return redirect('favourites')

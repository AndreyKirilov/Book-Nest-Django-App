from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from .forms import CreateBookForm, CreateAuthorForm
from .models import Author, Book


class CreateBookView(CreateView):
    model = Book
    form_class = CreateBookForm
    template_name = 'books/book-create.html'
    success_url = reverse_lazy('catalog')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff and not request.user.is_superuser:
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)


class CreateAuthorView(CreateView):
    model = Author
    form_class = CreateAuthorForm
    template_name = 'books/author-create.html'
    success_url = reverse_lazy('catalog')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff and not request.user.is_superuser:
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)


class DetailBookView(DetailView):
    model = Book
    template_name = 'books/book-display.html'
    context_object_name = 'book'

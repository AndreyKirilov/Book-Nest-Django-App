from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect

from E_Book_App.books.models import Book


def index(request):
    return render(request, 'common/index.html')


@login_required()
def catalog_view(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'common/catalog.html', context=context)

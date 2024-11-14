from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from .forms import CreateBookForm


def is_staff_or_superuser(user):
    return user.is_staff or user.is_superuser


@user_passes_test(is_staff_or_superuser)
def create_book_view(request):
    form = CreateBookForm(request.POST or None, request.FILES or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('catalog')

    context = {'form': form}
    return render(request, 'books/book-create.html', context=context)

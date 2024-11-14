from django import forms
from E_Book_App.books.models import Book


class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'publication_date', 'cover_image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Book Title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Book Author'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Book Description'}),
            'publication_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': "Book's Publication Date"}),
            'cover_image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Book Cover Image'})
        }

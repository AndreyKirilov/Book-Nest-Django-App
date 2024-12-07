from django import forms
from E_Book_App.books.models import Book, Author


class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'publication_date', 'cover_image']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Book Title'}),
            'author': forms.TextInput(attrs={'placeholder': "Book Author's pk"}),
            'description': forms.TextInput(attrs={'placeholder': 'Book Description'}),
            'publication_date': forms.DateInput(attrs={'placeholder': "Book's Publication Date", 'type': 'date'}),
            'cover_image': forms.FileInput(attrs={'placeholder': 'Book Cover Image'})
        }


class CreateAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'bio']
        widgets = {
            'name': forms.TextInput(attrs={"placeholder": "Author Name"}),
            'bio': forms.TextInput(attrs={"placeholder": "Author Bio"})
        }

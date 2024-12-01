from django.test import TestCase
from E_Book_App.books.models import Author, Book


class AuthorModelTest(TestCase):

    def test__valid__str__method(self):
        author = Author.objects.create(name='John Smith',
                                       bio='some bio')

        self.assertEqual(str(author), author.name)


class BookModelTest(TestCase):

    def test__valid__str__method(self):
        author = Author.objects.create(name='John Smith', bio='some bio')
        book = Book.objects.create(title='Some title', author=author,
                                   description='some description', publication_date='2005-07-06')

        self.assertEqual(str(book), book.title)

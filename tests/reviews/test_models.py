from django.test import TestCase
from E_Book_App.books.models import Book, Author
from E_Book_App.users.models import AppUser
from E_Book_App.reviews.models import Review


class ReviewModelTest(TestCase):

    def test__valid__str__method(self):
        author = Author.objects.create(name='John Smith', bio='some bio')
        book = Book.objects.create(title='Some title', author=author, description='some description',
                                   publication_date='2005-07-06')

        user = AppUser.objects.create(email='user@example.com')
        review = Review.objects.create(book=book, user=user, body='some text',
                                       created_at='2024-11-24 15:11:31.252987 +00:00',
                                       updated_at='2024-11-24 15:11:31.252987 +00:00')

        self.assertEqual(str(review), f'A review for {review.book.title}')

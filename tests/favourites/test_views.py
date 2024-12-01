from datetime import datetime
from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse

from E_Book_App.users.models import AppUser
from E_Book_App.books.models import Book, Author
from E_Book_App.favourites.models import Favourites


class TestAddToWishlistView(TestCase):
    def setUp(self):
        self.user = AppUser.objects.create_user(email='user@example.com', password='some_password')
        self.author = Author.objects.create(name='author1', bio="author 1 bio")
        self.book = Book.objects.create(title='Some title', author=self.author, description="Some desc",
                                        publication_date='2024-12-01', cover_image='book_image.jpg')

        self.client.login(email='user@example.com', password='some_password')

    def test__add__to__wishlist(self):
        self.assertTrue(self.user.is_authenticated)
        self.assertEqual(Favourites.objects.count(), 0)
        response = self.client.get(reverse('favourites_add', kwargs={'book_id': self.book.id}))

        self.assertEqual(Favourites.objects.count(), 1)
        self.assertRedirects(response, reverse('favourites'))


class TestRemoveFromWishlistView(TestCase):

    def setUp(self):
        # Set up test data
        self.user = AppUser.objects.create_user(email='user1@example.com', password='some_password')
        self.author = Author.objects.create(name='author1', bio='some author bio')
        self.book = Book.objects.create(title='Some title', author=self.author, description='some desc',
                                        publication_date='2024-12-01')
        self.favourite = Favourites.objects.create(user=self.user, book=self.book, created_on=datetime.now())

        self.client.login(username='user1@example.com', password='some_password')

    def test__remove__from_wishlist(self):
        self.assertEqual(Favourites.objects.count(), 1)

        response = self.client.get(reverse('favourites_remove', kwargs={'book_id': self.book.id}))

        self.assertEqual(Favourites.objects.count(), 0)
        self.assertRedirects(response, reverse('favourites'))

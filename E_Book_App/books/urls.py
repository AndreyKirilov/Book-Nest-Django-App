from django.urls import path
from E_Book_App.books import views


urlpatterns = [
    path('create-book/', views.create_book_view, name='book-create'),
]

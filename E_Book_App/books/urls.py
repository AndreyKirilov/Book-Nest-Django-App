from django.urls import path
from E_Book_App.books import views


urlpatterns = [
    path('create-book/', views.CreateBookView.as_view(), name='book-create'),
    path('create-author/', views.CreateAuthorView.as_view(), name='author-create'),
    path('details/<int:pk>/', views.DetailBookView.as_view(), name='book-details'),
]

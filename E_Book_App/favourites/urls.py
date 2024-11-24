from django.urls import path
from . import views

urlpatterns = [
    path('', views.FavouritesView.as_view(), name='favourites'),
    path('add/<int:book_id>/', views.add_to_wishlist_view, name='favourites_add'),
    path('remove/<int:book_id>/', views.remove_from_wishlist_view, name='favourites_remove'),
]

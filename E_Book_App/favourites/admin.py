from django.contrib import admin
from .models import Favourites


@admin.register(Favourites)
class FavouritesAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'created_on']
    list_filter = ['user', ]

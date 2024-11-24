from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('E_Book_App.common.urls')),
    path('users/', include('E_Book_App.users.urls')),
    path('books/', include('E_Book_App.books.urls')),
    path('favourites/', include('E_Book_App.favourites.urls')),
    path('reviews/', include('E_Book_App.reviews.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

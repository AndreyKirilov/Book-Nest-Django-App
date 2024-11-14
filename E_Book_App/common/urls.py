from django.urls import path
from E_Book_App.common import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog_view, name='catalog'),

]

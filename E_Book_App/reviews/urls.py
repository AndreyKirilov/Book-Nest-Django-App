from django.urls import path
from E_Book_App.reviews import views

urlpatterns = [
    path('api/', views.ReviewListCreateAPIView.as_view(), name='api-review-list-create'),
    path('api/<int:pk>/', views.ReviewDetailAPIView.as_view(), name='api-review-detail'),
    path('add/<int:book_id>/', views.review_page_view, name='review-page'),
    path('edit/<int:review_id>/', views.edit_review_view, name='review-edit'),
    path('delete/<int:review_id>/', views.delete_review_view, name='review-delete')
]

from django.urls import path
from E_Book_App.users import views

urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name='user-register'),
    path('login/', views.LoginUserView.as_view(), name='user-login'),
    path('logout/', views.logout_view, name='user-logout'),
    path('profile-page/', views.profile_page, name='user-profile-page'),
    path('profile-edit/', views.profile_edit_view, name='user-edit-page'),
    path('profile-delete/', views.profile_delete_view, name='user-delete-page')
]

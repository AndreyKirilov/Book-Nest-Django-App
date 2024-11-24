from django.contrib import admin

from E_Book_App.users.models import AppUser, Profile


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_staff']
    list_filter = ['email', ]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'bio']
    list_filter = ['first_name', 'last_name']
    ordering = ['first_name', ]

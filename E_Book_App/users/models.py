from django.contrib.auth.models import AbstractBaseUser, Group, PermissionsMixin
from django.db import models
from django.core.validators import MinLengthValidator

from .managers import AppUserManager


class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(null=False, blank=False, unique=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AppUserManager()


class Profile(models.Model):
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        validators=[MinLengthValidator(2, message="First name cannot be less than 2 char long!")])

    last_name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        validators=[MinLengthValidator(2, message="Last name cannot be less than 2 char long!")])

    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    bio = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        validators=[MinLengthValidator(10, message="Bio cannot be less than 10 char long!")])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

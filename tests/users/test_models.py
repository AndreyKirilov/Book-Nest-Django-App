from django.test import TestCase
from E_Book_App.users.models import AppUser, Profile


class ProfileModelTest(TestCase):

    def test__valid__str__method(self):
        user = AppUser.objects.create(email='user@example.com')
        profile = Profile.objects.create(user=user, first_name='Pesho', last_name='Petrov',  bio='some profile bio')

        self.assertEqual(str(profile), f"{profile.first_name} {profile.last_name}")

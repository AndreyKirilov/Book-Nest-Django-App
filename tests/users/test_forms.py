from django.test import TestCase
from E_Book_App.users.models import AppUser, Profile
from E_Book_App.users.forms import EditUserForm


class TestAppUserForm(TestCase):

    def test__save__method__with__commit__true(self):
        user = AppUser.objects.create(email='user@example.com')
        profile = Profile.objects.create(first_name='Pesho', last_name='Petrov', user=user)

        self.assertTrue(Profile.objects.filter(user=user).exists())
        self.assertEqual(profile.first_name, 'Pesho')
        self.assertEqual(profile.last_name, 'Petrov')
        self.assertEqual(profile.user, user)

    def test_save_with_commit_false(self):
        user = AppUser.objects.create(email='user@example.com')
        self.assertFalse(Profile.objects.filter(user=user).exists())


class TestEditUserForm(TestCase):

    def test__form__initialization__when__user__exists(self):
        user = AppUser(email='user@example.com')
        profile = Profile(first_name='Gosho', last_name='Georgiev', user=user, bio='some bio',
                          profile_image='path/to/profile_image.jpg')
        form = EditUserForm(user=user)

        self.assertEqual(form.fields['first_name'].initial, profile.first_name)
        self.assertEqual(form.fields['last_name'].initial, profile.last_name)
        self.assertEqual(form.fields['bio'].initial, profile.bio)
        self.assertEqual(form.fields['profile_image'].initial, profile.profile_image)

    def test__form__initialization__when__user__not__exists(self):
        form = EditUserForm()

        self.assertIsNone(form.fields['first_name'].initial)
        self.assertIsNone(form.fields['last_name'].initial)
        self.assertIsNone(form.fields['bio'].initial)
        self.assertIsNone(form.fields['profile_image'].initial)

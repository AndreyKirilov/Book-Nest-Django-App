from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from .models import Profile

AppUserModel = get_user_model()


class AppUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, min_length=2)
    last_name = forms.CharField(max_length=50, min_length=2)
    password1 = forms.CharField(widget=forms.PasswordInput, error_messages={'required': 'Password field is required',
                                                                            'min_length': 'Password must be at least 8 chars long'},
                                label="Password")

    class Meta:
        model = AppUserModel
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=commit)

        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

        profile = Profile(first_name=first_name, last_name=last_name, user=user)

        if commit:
            profile.save()

        return user


class LogoutUserForm(forms.Form):
    pass


class EditUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=50)
    bio = forms.CharField(max_length=500)
    profile_image = forms.ImageField(required=False)

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'bio', 'profile_image']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(EditUserForm, self).__init__(*args, **kwargs)

        if user:
            profile = user.profile
            self.fields['first_name'].initial = profile.first_name
            self.fields['last_name'].initial = profile.last_name
            self.fields['bio'].initial = profile.bio
            self.fields['profile_image'].initial = profile.profile_image


class DeleteUserForm(forms.Form):
    pass

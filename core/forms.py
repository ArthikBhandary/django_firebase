from django import forms
from django.contrib.auth.forms import AuthenticationForm

from core.models import Profile

from allauth.account.forms import SignupForm


class SignUpProfileForm(SignupForm):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)


class ProfileForm(forms.ModelForm):
    model = Profile


class FirebaseAuthenticationForm(AuthenticationForm):
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()

        return self.cleaned_data

from django import forms

from core.models import Profile

from allauth.account.forms import SignupForm


class SignUpProfileForm(SignupForm):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)


class ProfileForm(forms.ModelForm):
    model = Profile

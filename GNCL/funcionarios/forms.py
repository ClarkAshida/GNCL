# forms.py
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username']

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        required=False,
        help_text="Leave it blank if you don't want to change your password."
    )

from django import forms
from crispy_forms.helper import FormHelper
from django.contrib.auth import (authenticate, get_user_model, login, logout)

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                                       'class': 'form-control my-2'}))
    password = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Password',
                                                                       'class': 'form-control my-2', 'type': 'password'}))

    helper = FormHelper()

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        if not user:
            raise forms.ValidationError("This user does not exist!")

        if not user.check_password(password):
            raise forms.ValidationError("Incorrect password!")

        if not user.is_active:
            raise forms.ValidationError("This user is no longer active!")

        return super(UserLoginForm, self).clean()
from django import forms
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class LoginForms(AuthenticationForm):
    # email = forms.EmailField(widget=forms.EmailInput(attrs={'focus': True}))

    class Meta:
        model = CustomUser
        fields = ['email', 'password']


class SignUpForms(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'focus': True}))
    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']


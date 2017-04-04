from django.contrib.auth.models import User
from .models import UserProfile

from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['username', 'email', 'password', ]


class LoginForm(forms.ModelForm):
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['username', 'password']

class ProfileForm(forms.ModelForm):
    address = forms.CharField(max_length=300,widget= forms.Textarea)

    class Meta:
        model = UserProfile
        fields=['address','phone']

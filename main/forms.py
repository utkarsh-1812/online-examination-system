from django.contrib.auth.forms import UserCreationForm, UserChangeForm,AuthenticationForm

from .models import User_new
from django import forms
from django.core.validators import RegexValidator


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User_new
        fields = ('email',)

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User_new
        fields = [
            'email',
            'Name',
            'is_student',
            'is_teacher',
            'Institute_Name',
            'Institute_ID',
            'phone',
            'password1',
            'password2',
        ]

class LoginForm(AuthenticationForm):
    class Meta:
        model = User_new
        fields = [
            'email',
            'Name',
            'password',
        ]
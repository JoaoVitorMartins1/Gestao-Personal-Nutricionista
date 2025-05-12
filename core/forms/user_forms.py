from django import forms
from django.contrib.auth.forms import UserCreationForm
from core.models import User

class UsuarioPersonalForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

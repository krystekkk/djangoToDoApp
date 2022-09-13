from django.forms import ModelForm, TextInput, EmailField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Todos


class TodosForm(ModelForm):
    class Meta:
        model = Todos
        fields = ['name']
        labels = {
            'name': 'New todo'
        }


class RegisterForm(UserCreationForm):
    email = EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

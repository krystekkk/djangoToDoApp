from django.forms import ModelForm, TextInput
from .models import Todos


class TodosForm(ModelForm):
    class Meta:
        model = Todos
        fields = ['name']

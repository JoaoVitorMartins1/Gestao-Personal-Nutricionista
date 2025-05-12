from django import forms
from django.forms import DateInput

from ..models import Aluno


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'  # Sem colchetes (não é uma lista)
        exclude = ['personal', 'data_cadastro']
        widgets = {
            'data_nascimento': DateInput(attrs={'type': 'date'})
        }
from django import forms
from django.forms import DateInput

from ..models import Plano

class PlanoForm(forms.ModelForm):
    class Meta:
        model = Plano
        fields = '__all__'
        exclude = ['aluno']
        widgets = {
            'data_inicio': DateInput(attrs={'type': 'date'}),
            'data_vencimento': DateInput(attrs={'type': 'date'})
        }
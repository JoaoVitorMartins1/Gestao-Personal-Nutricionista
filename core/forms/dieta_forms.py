from ..models import Dieta
from django import forms


class DietaForm(forms.ModelForm):
    class Meta:
        model = Dieta
        fields = '__all__'
        exclude = ['aluno','data_criacao']

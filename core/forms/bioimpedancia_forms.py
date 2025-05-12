from django.forms import DateInput

from ..models import Bioimpedancia
from django import forms



class BioimpedanciaForm(forms.ModelForm):
    class Meta:
        model= Bioimpedancia
        fields= '__all__'
        exclude=['aluno']
        widgets = {
            'data_medicao': DateInput(attrs={'type': 'date'})
        }
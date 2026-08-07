from django import forms
from .models import Crianca


class CriancaForm(forms.ModelForm):
    class Meta:
        model = Crianca
        fields = ['nome', 'idade', 'provincia', 'localidade', 'finalidade', 'linguagem']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'O teu nome completo'}),
            'idade': forms.NumberInput(attrs={'placeholder': 'A tua idade', 'min': 10, 'max': 17}),
            'localidade': forms.TextInput(attrs={'placeholder': 'A tua localidade'}),
            'finalidade': forms.TextInput(attrs={'placeholder': 'Para que fins vais usar a linguagem?'}),
        }
        labels = {
            'nome': 'Nome completo',
            'idade': 'Idade',
            'provincia': 'Provincia',
            'localidade': 'Localidade',
            'finalidade': 'Para que fins?',
            'linguagem': 'Linguagem escolhida',
        }
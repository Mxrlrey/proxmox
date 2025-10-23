from django import forms
from .models import Equipe

class EquipeForm(forms.ModelForm):
    class Meta:
        model = Equipe
        fields = ['nome', 'usuario', 'membro1', 'membro2']
        labels = {
            'nome': 'Nome da equipe',
            'usuario': 'Nome que o usuário utilizou para cadastrar',
            'membro1': 'Membro 1',
            'membro2': 'Membro 2',
        }

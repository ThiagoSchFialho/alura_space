from django import forms
from apps.galeria.models import Fotografia

class FotografiaForm(forms.ModelForm):
    class Meta:
        model = Fotografia   # Nome do model
        exclude = ['publicada',]   # Campos que serão ignorados
        labels = {   # Como os labels aparecerão
            'nome': 'Nome',
            'legenda': 'Legenda',
            'categoria': 'Categoria',
            'descricao': 'Descrição',
            'foto': 'Foto',
            'data_fotografia': 'Data de registro',
            'usuario': 'Usuário',
        }

        widgets = {   # Campos do formulário
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'legenda': forms.TextInput(attrs={'class':'form-control'}),
            'categoria': forms.Select(attrs={'class':'form-control form-control-select'}),
            'descricao': forms.Textarea(attrs={'class':'form-control form-control-textarea'}),
            'foto': forms.FileInput(attrs={'class':'form-control form-control-file'}),
            'data_fotografia': forms.DateInput(
                format = '%d/%m/%Y',
                attrs={
                    'type': 'date',
                    'class':'form-control'
                    }
                ),
            'usuario': forms.Select(attrs={'class':'form-control form-control-select'})
        }


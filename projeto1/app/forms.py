from django import forms
from .models import Tarefa

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = '__all__' #todos os campos do nosso models Tarefa seja exibido no formulário de cadastro
        widgets = {
            "data": forms.DateInput(attrs={'type': 'date'})
        }
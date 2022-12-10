from django.shortcuts import render, redirect
from .forms import TarefaForm
from .models import Tarefa


def cadastrar_tarefa(request):
    if request.method == "POST":
        form_tarefa = TarefaForm(request.POST)
        if form_tarefa.is_valid():
            form_tarefa.save()
            return redirect('listar_tarefa')
    else:
        form_tarefa = TarefaForm()
        
    return render(request, 'form_cadastro.html', {'form_tarefa': form_tarefa})#aqui estamos enviando como paramêtro um objeto to tipo form_tarefa com propriedade do form_tarefa

def listar_tarefa(request):
    tarefas = Tarefa.objects.all()#isso aqui faz com que buscamos todas as tarefas no banco de dados e armazene na variável tarefas
    
    return render(request, 'lista_tarefas.html', {'tarefas': tarefas})
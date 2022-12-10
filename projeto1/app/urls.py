#urls da aplicação
from django.urls import path
from .views import cadastrar_tarefa, listar_tarefa

urlpatterns = [
    path('cadastrar_tarefa', cadastrar_tarefa, name='cadastrar_tarefa'),
    path('listar_tarefas', listar_tarefa, name='listar_tarefa'),
]
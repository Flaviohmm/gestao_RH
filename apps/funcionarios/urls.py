from django.urls import path
from .views import FuncionarioEdit, FuncionariosList

urlpatterns = [
    path('', FuncionariosList.as_view(), name='list_funcionarios'),
    path('editar/<int:pk>/', FuncionarioEdit.as_view(), name='update_funcionario')
]

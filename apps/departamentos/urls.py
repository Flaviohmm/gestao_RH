from django.urls import path
from .views import DepartamentoCreate, DepartamentosList

urlpatterns = [
    path('list', DepartamentosList.as_view(), name='list_departamentos'),
    path('novo', DepartamentoCreate.as_view(), name='create_departamento'),
]
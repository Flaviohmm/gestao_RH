from django.urls import path
from .views import (
    HoraExtraList,
    HoraExtraEdit
)

urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    path('editar/<int:pk>/', HoraExtraEdit.as_view(), name='update_hora_extra'),
]

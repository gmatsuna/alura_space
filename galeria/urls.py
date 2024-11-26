from django.urls import path
from galeria.views import home, imagem, buscar

urlpatterns = [
    path('', home, name='home'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
]

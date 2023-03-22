from django.urls import path
from galeria.views import index, imagem, buscar, busca_tag

urlpatterns = [
    path('', index, name='index'),
    path('index', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar, name="buscar"),
    path('tags/<str:tag>', busca_tag, name="tag")
]

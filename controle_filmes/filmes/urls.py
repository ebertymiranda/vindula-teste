from django.urls import path
from .views import lista_filmes, cadastra_filme, importa_excel, lista_filmes_autocomplete, relatorio_filmes

urlpatterns = [
    path('lista/', lista_filmes, name='lista_filmes'),
    path('cadastra/', cadastra_filme, name='cadastra_filme'),
    path('importa_excel/', importa_excel, name='importa_excel'),
    path('lista_filmes_autocomplete/', lista_filmes_autocomplete, name='lista_filmes_autocomplete'),
    path('relatorio', relatorio_filmes, name='relatorio_filmes'),
]

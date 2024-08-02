from django.urls import path
from ferramentas.views import termos, submit, relatorio,lista_relatorios

app_name = 'ferramentas'
urlpatterns = [
    path('relatorio/', relatorio, name='relatorio'),  # Ferramentas
    path('termos/', termos, name='termos'),  # Termos
    path('submit/', submit, name='submit'),  # Submissão do formulário
    path('relatorio/', relatorio, name='relatorio'),  # Relatório
    path('lista_relatorios/', lista_relatorios, name='lista_relatorios'),  # Lista de relatórios
    
]
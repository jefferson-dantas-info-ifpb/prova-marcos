from django.urls import path
from . import views

urlpatterns = [
    path("irmaos-de-matheus-nao-vacinados", views.nao_vacinados_irmaos_de_matheus),
    path("vacinados-idade-2-a-8", views.vacinados_idade_2_a_8),
    path("vacinados-poliomielite-idade-menores-3", views.vacinados_poliomielite_idade_menores_3),
    path("vacinados-bairro-limeira", views.vacinados_bairro_limeira),
    path("quantidade-criancas-vacinadas", views.quantidade_criancas_vacinadas)
]

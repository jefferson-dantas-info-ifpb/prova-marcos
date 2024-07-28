from django.shortcuts import render
from .models import Crianca

# Create your views here.
def nao_vacinados_irmaos_de_matheus(request):
    criancas = Crianca.objects.filter(nome_mae="Maria Antonieta", vacina="")
    return render(request, "criancas.html", {
        'titulo': 'Irmãos de Matheus não vacinados',
        'criancas': criancas
    })

def vacinados_idade_2_a_8(request):
    criancas = Crianca.objects.filter(idade_crianca__gte=2, idade_crianca__lte=8).exclude(vacina="")
    return render(request, "criancas.html", {
        'titulo': 'Crianças vacinadas com idade entre 2 e 8 anos',
        'criancas': criancas
    })

def vacinados_poliomielite_idade_menores_3(request):
    criancas = Crianca.objects.filter(vacina="Poliomielite", idade_crianca__lt=3).exclude(vacina="")
    return render(request, "criancas.html", {
        'titulo': 'Crianças vacinadas contra poliomielite menores que 3 anos de idade',
        'criancas': criancas
    })

def vacinados_bairro_limeira(request):
    criancas = Crianca.objects.filter(bairro="Limeira").exclude(vacina="")
    return render(request, "criancas.html", {
        'titulo': 'Crianças vacinadas do bairro limeira',
        'criancas': criancas
    })

def quantidade_criancas_vacinadas(request):
    qtd_criancas = Crianca.objects.exclude(vacina="").count()
    return render(request, "criancas-nao-vacinadas.html", {
        'titulo': 'Quantidade de crianças vacinadas',
        'qtd_criancas': qtd_criancas
    })

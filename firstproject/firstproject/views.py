from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return render(request, 'index.html')


def articles(request, year):
    return HttpResponse(f'Ano passado foi {year}')


def ledDoBanco(nome):
    lista_nomes = [
        {'nome': 'Ana', 'idade': 20},
        {'nome': 'Pedro', 'idade': 25},
        {'nome': 'Joaquim', 'idade': 27},
    ]
    for pessoa in lista_nomes:
        if pessoa['nome'] == nome:
            return pessoa
    else:
        return{'nome':'Pessoa Não Encontrado', 'idade': 0}


def fname(request, nome):
    result = ledDoBanco(nome)
    print(result)
    if result['idade'] > 0:
        return HttpResponse(f"A pessoa foi encontrada, ela tem {str(result['idade'])} anos ")
    else:
        return HttpResponse(result['nome'])

def fname2(request, nome):
    idade = ledDoBanco(nome)['idade']
    return render(request,'pessoa.html',{'v_idade': idade})
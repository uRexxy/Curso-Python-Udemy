from encodings import utf_8
import os
from time import sleep
import json

lista = []
lista_inteira = []

cont = 0


def desfazer(lista, lista_inteira):
    if lista:
        print(f'Removendo {lista[-1]}')
        print()
        global cont
        cont += 1
        lista.pop()
        if cont % 2 == 0:
            lista_inteira.pop()
        for i in lista:
            print(f'- {i}')
    else:
        print('Nada para remover.')


def refazer(lista, lista_inteira):
    if lista:
        global cont
        print(f'refazendo {lista_inteira[-1]}')
        lista.append(lista_inteira[-1])
        for i in lista:
            print(f'- {i}')
        cont += 1
    else:
        print('Nada para refazer.')


def listar(lista):
    if lista:
        print()
        for i in lista:
            print(f'- {i}')
    else:
        print('Sua lista de tarefas está vazia.')


def excluir(lista, lista_inteira):
    if lista:
        lista.clear()
        lista_inteira.clear()
        print('Sua lista de tarefas foi excluida.')
    else:
        print('Sua lista de tarefas já está vazia.')


while True:

    r = str(input('Escolha uma ação (refazer, desfazer, listar, excluir, clear): '))

    if r == 'refazer':
        refazer(lista, lista_inteira)
    elif r == 'desfazer':
        desfazer(lista, lista_inteira)
    elif r == 'listar':
        listar(lista)
    elif r == 'clear':
        os.system('cls')
    elif r == 'excluir':
        excluir(lista, lista_inteira)
    else:
        lista.append(r)
        lista_inteira.append(r)
        print(f'Adicionando {r}\n')
        for i in lista:
            print(f'- {i}')
    sleep(0.5)
    print()

    CAMINHO_ARQUIVO = "C:\\Users\\Tadin\\OneDrive\\Documentos\\Curso Python Udemy\\ExercíciosUDEMY\\"
    CAMINHO_ARQUIVO += "Lista_tarefas.Json"

    with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
        json.dump(lista, arquivo, indent=2, ensure_ascii=False)

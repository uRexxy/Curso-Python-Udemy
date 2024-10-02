from time import sleep
import os
from random import randint
from tkinter import *


janela = Tk()
janela.title('Crie seu Pimba')
janela.geometry('600x400')
janela.configure(background='#141313')

janela.mainloop()

fazenda = []


class Pimba:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterarNome(self):
        nomeNovo = str(
            input('Digite um novo nome para seu Pimba: ')).capitalize()
        nomeVelho = self.nome
        self.nome = nomeNovo
        return print(f'Você alterou o nome do seu Pimba de {nomeVelho} para {self.nome}')

    def verfome(self):
        fome_atual = self.fome
        if fome_atual <= 2:
            return print(f'{self.nome.capitalize()} está com {fome_atual} de fome. {self.nome.capitalize()} Precisa comer!')
        if fome_atual <= 6:
            return print(f'{self.nome.capitalize()} está com {fome_atual} de fome. Dê comida para {self.nome.capitalize()}')
        if fome_atual >= 7:
            return print(f'{self.nome.capitalize()} está com {fome_atual} de fome. {self.nome.capitalize()} está satisfeito.')

    def verSaude(self):
        saude_atual = self.saude
        if saude_atual <= 2:
            return print(f'{self.nome.capitalize()} está doente!')
        if saude_atual <= 6:
            return print(f'{self.nome.capitalize()} está bem.')
        if saude_atual >= 7:
            return print(f'{self.nome.capitalize()} está muito bem!')

    def verIdade(self):
        return print(f'{self.nome.capitalize()} está com {self.idade} anos de idade.')

    def verHumor(self):
        saude_atual = self.saude
        fome_atual = self.fome
        humor_atual = fome_atual + saude_atual
        if humor_atual <= 4:
            return print(f'{self.nome.capitalize()} está de muito mal humor.')
        if 5 <= humor_atual <= 15:
            return print(f'{self.nome.capitalize()} está com o humor normal.')
        if humor_atual >= 16:
            return print(f'{self.nome.capitalize()} está de muito bom humor.')

    def darComida(self):
        print(f'A fome atual de {self.nome} é: {self.fome}')
        dar_comida = input(f'Quanto de comida quer dar ao {self.nome}? ')
        dar_comida = int(dar_comida)
        if self.fome >= 0 and self.fome <= 10:
            self.fome += dar_comida
            if self.fome < 0:
                self.fome = 0
            elif self.fome > 10:
                self.fome = 10

        if dar_comida < 0:
            print(f'Não podes dar {dar_comida} de comida para {self.nome}')

    def brincar(self):
        tempo_brincar = input(
            f'Por quanto tempo deseja brincar com {self.nome}?  [0 á 10 min] ').strip()
        tempo_brincar = int(tempo_brincar)
        if tempo_brincar < 1:
            tempo_brincar = 1
        elif tempo_brincar > 10:
            tempo_brincar = 10
        self.saude += (tempo_brincar / 2)

    def str(self):
        print(f'Nome: {self.nome} \n'
              f'Fome: {self.fome} \n'
              f'Saúde: {self.saude} \n'
              f'Idade: {self.idade} \n'
              f'Humor: {self.saude + self.fome}')


def criarFazenda(num_pimbas):
    global fazenda
    fazenda = []
    for n in range(1, num_pimbas+1):
        nome = str(input(f'Digite o nome do {n}° Pimba: '))
        fazenda.append(Pimba(nome, randint(1, 10),
                       randint(1, 10), randint(1, 100)))


def criarPimba(nome, fome, saude, idade):
    Pimba1 = Pimba(nome, fome, saude, idade)
    while True:
        print()
        sleep(1.5)
        print('O que você deseja fazer com o seu Pimba?')
        print('1 - Alterar o nome \n'
              '2 - Verificar a fome \n'
              '3 - Verificar a saúde \n'
              '4 - Ver a idade \n'
              '5 - Ver humor \n'
              '6 - Dar Comida \n'
              '7 - Brincar \n'
              '0 - Sair')
        r = str(input('Sua opção: ')).strip()
        print()
        if r == '1':
            os.system('cls')
            Pimba1.alterarNome()
        elif r == '2':
            os.system('cls')
            Pimba1.verfome()
        elif r == '3':
            Pimba1.verSaude()
            os.system('cls')
        elif r == '4':
            os.system('cls')
            Pimba1.verIdade()
        elif r == '5':
            os.system('cls')
            Pimba1.verHumor()
        elif r == '6':
            os.system('cls')
            Pimba1.darComida()
        elif r == '7':
            os.system('cls')
            Pimba1.brincar()
        elif r == '0':
            print('Saindo...')
            sleep(1.5)
            break
        elif r == '000':
            os.system('cls')
            Pimba1.str()


# criarPimba('Cleito', 6, 5, 6)

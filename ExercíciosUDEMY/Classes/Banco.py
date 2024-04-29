import os
from time import sleep


class Usuario:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo
    

    def sacar(self, saque):
        if saque > self.saldo:
            print('Valor inválido/Saldo insuficiente')
        else:
            self.saldo -= saque
            print(f'Saque de R${saque:.2f} efetuado. Restam R${self.saldo:.2f}')

    

    def depositar(self, depo):
        if depo > 0:
            self.saldo += depo
            print(f'Deposito de R${depo:.2f} efetuado com sucesso.')
        else:
            print('Deposito inválido.')

    
    def ver_saldo(self):
        return print(f'Nome do cliente: {self.nome}\nSaldo da conta: R${self.saldo:.2f}')

              

usuario1 = Usuario('João', 12000)



print('-'*40)
print(f'{"BANCO CRUZEIRO DO SUL":^40}')
print('-'*40)


print('Bem vindo ao banco Cruzeiro do Sul!')
while True:
    print('Qual operação deseja fazer?\n\t1- Sacar\n\t2- Depositar\n\t3- Ver saldo\n\t4 - Sair')

    r = str(input('Sua opção: ')).strip()
    if r == '1':
        os.system('cls')
        saque = float(input(print('Quanto R$ você gostaria de sacar? R$')))
        usuario1.sacar(saque)
    elif r == '2':
        os.system('cls')
        deposito = float(input(print('Quanto R$ você gostaria de depositar? R$')))
        usuario1.depositar(deposito)
    elif r == '3':
        os.system('cls')
        usuario1.ver_saldo()
    elif r == '4':
        os.system('cls')
        print('Saindo...')
        sleep(1)
        break
    sleep(1)
    print('\t')
    sleep(1)

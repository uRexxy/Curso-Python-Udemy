class usuario:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo
    

    def sacar(self, saque):
        
        if saque > self.saldo:
            print('Valor inválido/Saldo insuficiente')
        elif saque <= self.saldo:
            self.saldo = saque - self.saldo
            print(f'Saque de R${saque:.2f} efetuado. Restam R${self.saldo:2f}')
    

    def depositar(self, deposito):
        if deposito > 0:
            self.saldo += deposito

    
    def ver_saldo(self, saldo):
        print(f'Nome do cliente: {self.nome}\nSaldo da conta: {saldo}')

usuario1 = usuario('João', 12500)
    
print('-'*40)
print(f'{"BANCO CRUZEIRO DO SUL":^40}')
print('-'*40)

while True:
    print('Bem vindo ao banco Cruzeiro do Sul!')
    print('Qual operação deseja fazer?\n\t1- Sacar\n\t2- Depositar\n\t3- Ver saldo')

    while True:
        r = str(input('Sua opção: ')).strip()
        if r == '1':
            usuario.sacar(23, 3)

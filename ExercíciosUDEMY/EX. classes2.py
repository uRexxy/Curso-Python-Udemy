class bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocarCor(self):
        nova_cor = str(input('Digite a nova cor: '))
        self.cor = nova_cor

    def mostraCor(self):
        print(f'A cor desta bola é {self.cor}')


bola1 = bola('Azul', 22, 'borracha')
bola2 = bola('Vermelha', 30, 'Plastico')

bola2.trocarCor()
bola2.mostraCor()

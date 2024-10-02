import pandas as pd
from time import sleep


class Submarino:
    def __init__(self, nome, modelo, profundidade):
        self.nome = nome
        self.modelo = modelo
        self.profundidade = profundidade

    def entrar(self):
        return 'Bem-vindo a bordo capitão, todos os sistemas online.'

    def ligar(self):
        return 'ligando motores.'

    def deep(self):
        if self.profundidade < deep_atual:
            return 'danos eminentes, suba imediatamente!'
        if self.profundidade > deep_atual:
            return f'prosseguindo na profundidade {deep_atual}m'


deep_atual = 500

sub1 = Submarino('Prawn', 'Traje Robótico', 1000)
sub2 = Submarino('Seamoth', 'Submarino leve', 300)
sub3 = Submarino('Cyclops', 'Submarino Grande', 600)

dic = {'Nome': [sub1.nome, sub2.nome, sub3.nome], 'Modelo': [sub1.modelo, sub2.modelo,
                                                             sub3.modelo], 'Profundidade Máxima': [sub1.profundidade, sub2.profundidade, sub3.profundidade]}
df = pd.DataFrame(data=dic)
print(df)
print('\n\n\n')
sleep(3)
print(sub3.entrar())
sleep(3)
print(sub3.ligar())
sleep(2)
print(sub3.deep())

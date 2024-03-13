

class Cliente:
    'Classe representa pessoa'

    def __init__(self, nome_cliente, cpf, endereco_cliente):
        self.nome_cliente = nome_cliente
        self.cpf = cpf
        self.endereco_cliente = endereco_cliente


class Locacao:
    'Classe que conduz a locacao para cada cliente'

    def __init__(self, automovel, data_locacao, data_devolucao):
        self.automovel = automovel
        self.data_locacao = data_locacao
        self.data_devolucao = data_devolucao


class Empresa:
    'Classe que representa a empresa locadora de veiculos'

    def __init__(self, nome_empresa, cnpj, endereco_empresa):
        self.nome_empresa = nome_empresa
        self.cnpj = cnpj
        self.endereco_empresa = endereco_empresa

    def checarDisponibilidade(self, Automovel):
        esta_disponivel = True
        if esta_disponivel == True:
            return True

    def realizarLocacao(self):
        print(
            f'Realizando locação de {modelo1.nome_marca} {modelo1.nome_modelo} placa {automovel1.num_placa} para {cliente1.nome_cliente}.')

    def cancelarLocacao(self):
        pass


class Automovel:
    def __init__(self, num_placa, cor, ano, tipo_combustivel, num_portas, quilometragem, renavam, chassi, valor_locacao):
        self.num_placa = num_placa
        self.cor = cor
        self.ano = ano
        self.tipo_combustivel = tipo_combustivel
        self.num_portas = num_portas
        self.quilometragem = quilometragem
        self.renavam = renavam
        self.chassi = chassi
        self.valor_locacao = valor_locacao


class Modelo:
    def __init__(self, nome_modelo, nome_marca):
        self.nome_modelo = nome_modelo
        self.nome_marca = nome_marca


class Marca:
    def __init__(self, nome_marca):
        self.nome_marca = nome_marca


cliente1 = Cliente('John', '111111111-1', 'Rua São paulo')
modelo1 = Modelo('Civic', 'Honda')
automovel1 = Automovel('QT1VIY9', 'Preto', '2007', 'Gasolina',
                       '4', '89000', '2637109', '786fwes44536', '400')
empresa1 = Empresa('Carros aluguel', '54664767657', 'Rua Rio')

empresa1.realizarLocacao()

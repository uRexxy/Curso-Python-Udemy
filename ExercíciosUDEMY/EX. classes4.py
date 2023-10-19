class bombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self):
        try:
            valor_cliente = float(input('Quantos Reais deseja abastecer? R$'))
        except ValueError:
            print('Digite um valor válido.')

        litros_no_veiculo = valor_cliente / self.valorLitro
        print(
            f'Com R${valor_cliente:.2f}, o tanque receberá {litros_no_veiculo:.2f}L de combustivel.')
        self.quantidadeCombustivel = self.quantidadeCombustivel - litros_no_veiculo

    def abastecerPorLitro(self):
        try:
            litro_cliente = int(input('Quantos litros deseja encher? '))
        except ValueError:
            print('Digite um valor inteiro para o litro.')

        valor_a_pagar = litro_cliente * self.valorLitro
        print(f'{litro_cliente}L custará R${valor_a_pagar:,.2f}')
        self.quantidadeCombustivel = self.quantidadeCombustivel - litro_cliente

    def alterarValor(self):
        novo_preco = float(
            input('Digite um novo valor/L para o combustivel: R$'))
        self.valorLitro = novo_preco
        print(f'O novo valor/L do combustivel agora é {self.valorLitro:.2f}.')

    def alterarCombustivel(self):
        novo_nome = str(
            input('Digite o novo nome para o combustivel: ')).capitalize()
        self.tipoCombustivel = novo_nome
        print(
            f'Você alterou o nome do combustivel para {self.tipoCombustivel}.')

    def alterarQndBomba(self):
        nova_quantidade_combustivel = float(input('Quantos litros de combustivel a bomba terá? '))
        self.quantidadeCombustivel = f'{nova_quantidade_combustivel:.2f}'
        print(f'Agora a bomba tem {self.quantidadeCombustivel}L de combustivel.')



bomba1 = bombaCombustivel('Etanol', 5.74, 800)


# bomba1.abastecerPorValor()
# bomba1.abastecerPorLitro()
# bomba1.alterarCombustivel()
# bomba1.alterarValor()
print(bomba1.quantidadeCombustivel)
bomba1.abastecerPorLitro()
print(bomba1.quantidadeCombustivel)
bomba1.abastecerPorValor()
print(bomba1.quantidadeCombustivel)
bomba1.alterarQndBomba()
print(bomba1.quantidadeCombustivel)

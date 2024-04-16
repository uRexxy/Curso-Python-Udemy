from itertools import zip_longest


def sumList(*args):
    """Recebe listas como argumento e soma elas com base na menor lista."""

    lista_somada = [sum(elemento) for elemento in zip(*args)]
    return lista_somada


lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4, 5, 90]
lista_c = [1, 2, 3, 4, 5, 12, 88, 22, 0]

print(sumList(lista_a, lista_b, lista_c))


def Sumlistlong(*args):
    """Recebe listas como argumento e soma elas com base na maior lista preenchendo valores vazios com zero"""

    lista_somada = [sum(valores) for valores in zip_longest(*args, fillvalue=0)]
    return lista_somada

print(Sumlistlong(lista_a,lista_b,lista_c))








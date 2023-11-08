import copy

# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = copy.deepcopy(produtos)
for dic in novos_produtos:
    novos_precos = dic.get('preco') + (dic.get('preco') * 10 / 100)
    novos_precos = f'{novos_precos:.2f}'
    dic.update({'preco': novos_precos})

for n in novos_produtos:
    print(n)

# Ordene os produtos por nome decrescente (do maior para menor)





# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

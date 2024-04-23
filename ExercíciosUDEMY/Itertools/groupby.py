from itertools import groupby

# Agrupar valores pela chave: groupby
alunos = [
    {'nome': 'João', 'nota': 'B'},
    {'nome': 'Maria', 'nota': 'A'},
    {'nome': 'Júlia', 'nota': 'D'},
    {'nome': 'Rafael', 'nota': 'B'},
    {'nome': 'Luis', 'nota': 'B'},
    {'nome': 'Ana', 'nota': 'A'},
    {'nome': 'Nathan', 'nota': 'C'},
    {'nome': 'Joyce', 'nota': 'B'}
]

def ordena(aluno):
    return aluno['nota']


alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados, key=ordena)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)

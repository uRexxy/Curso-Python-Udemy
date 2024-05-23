
import json


pessoa = {
    'nome': 'Rafael',
    'sobrenome': 'Moraes',
    'endereco': [
        {'rua': 'Tulipas', 'numero': 123},
        {'rua': 'Rosas', 'numero': 321}
    ],
    'altura': 1.72,
    'nascimento': '01/01/0001',
    'estudante': True,
    'nada': None
}


caminho_arquivo = "C:\\Users\\Tadin\\OneDrive\\Documentos\\Curso Python Udemy\\ExercíciosUDEMY\\WithOpen\\Contextmanager\\"
caminho_arquivo += "arquivo.json"

# criando um arquivo .json e colocando as informações nele
with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
    json.dump(pessoa, arquivo, indent=2)


# abrindo um arquivo .json
with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)
    print('#\n'*5)
    print(pessoa['nome'], pessoa['sobrenome'])

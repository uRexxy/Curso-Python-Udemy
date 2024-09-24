import json

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('João', 22)
p2 = Pessoa('Luisa', 28)
p3 = Pessoa('Jaime', 44)


pessoas = (vars(p1),
            p2.__dict__,
            p3.__dict__,
            )

path = "C:\\Users\\Tadin\\OneDrive\\Documentos\\Curso Python Udemy\\ExercíciosUDEMY\\Classes\\"
path += "Pessoas_ClassJSON"

with open(path, 'w', encoding='utf8') as arquivo:
    json.dump(pessoas, arquivo, indent=2, ensure_ascii=False)
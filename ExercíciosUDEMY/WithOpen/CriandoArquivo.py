from os import close


caminho_arquivo = "C:\\Users\\Tadin\\OneDrive\\Documentos\\Curso Python Udemy\\ExercíciosUDEMY\\WithOpen\\Contextmanager\\"
caminho_arquivo += 'arquivo1.txt'

# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load


# abrindo e fechando o arquivo (with open)
with open(caminho_arquivo, 'w+', encoding='utf-8') as arquivo:
    # escrevendo uma linha (.write)
    arquivo.write('Linha 1\r\n')
    arquivo.write('Olá, escrevendo no arquivo!\n')
    arquivo.write('Mais um pouco de escrita.\n')

    # escrivendo varias linhas usando um iteravel (.writelines)
    arquivo.writelines(
        ('Usando writelines aqui.\n', 'Aqui tambem!\n')
    )

    # movendo o cursor para o inicio do arquivo (.seek)
    arquivo.seek(0, 0)

    # lendo o arquivo inteiro (.read)
    print(arquivo.read())

    arquivo.seek(0, 0)

    # lendo o arquivo linha por linha (.readline)
    print(arquivo.readline())
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())

from time import sleep


def contador(inicio, passo, para, tempo=0):
    while inicio < para:
        print(inicio)
        inicio += passo
        print(inicio)
        sleep(tempo)
    print('Fim')


contador(10, 6, 20, 0.3)

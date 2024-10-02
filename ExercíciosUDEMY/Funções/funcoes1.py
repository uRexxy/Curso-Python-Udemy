def multi(*args):
    m = 1
    for n in args:
        m *= n
    return m


def par_impar(x):
    if x % 2 == 0:
        return f'O número {x} é par'
    else:
        return f'O número {x} é ímpar'


print(multi(2, 5, 6, 8))

print(par_impar(1))

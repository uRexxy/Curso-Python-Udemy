def accum(string):
    letras = []

    for i, char in enumerate(string):
        part = (char * (i + 1)).capitalize()

        letras.append(part)

    return '-'.join(letras)

print(accum('AbCd'))

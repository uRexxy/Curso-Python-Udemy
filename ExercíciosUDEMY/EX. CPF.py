
def verificador_cpf(cpfp):
    import re
    num = []
    cpf = cpfp
    cpf_string = str(cpf)
    cpf = re.sub(r'[^0-9]', '', cpf_string)
    nove_digitos = cpf[:9]
    if len(cpf) < 11 or len(cpf) > 11:
        print('CPF inválido.')
    else:
        for numero in nove_digitos:
            numero = int(numero)
            num.append(numero)
        cont = 10
        somacpf_um = 0

        for numero in num:
            somacpf_um += (numero * cont)
            cont -= 1
        somacpf_um = (somacpf_um * 10) % 11

        if somacpf_um > 9:
            somacpf_um = 0
        print(f'O primeiro digito do seu cpf é {somacpf_um}')
        num.clear()

        dez_digitos = nove_digitos + str(somacpf_um)
        for numero in dez_digitos:
            numero = int(numero)
            num.append(numero)
        cont = 11
        somacpf_dois = 0

        for numero in num:
            somacpf_dois += (numero * cont)
            cont -= 1
        somacpf_dois = (somacpf_dois * 10) % 11

        if somacpf_dois > 10:
            somacpf_dois = 0
        print(f'O segundo digito do seu cpf é {somacpf_dois}')


verificador_cpf('CPF aqui')

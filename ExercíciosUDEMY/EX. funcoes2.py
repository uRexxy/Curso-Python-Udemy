def binary_sum(a, b):
    """Receive the sum of two numbers and return the sum in binary"""
    soma = bin(a + b)
    return print(f'The sum of {a} and {b} is {soma[2:]} in binary')


binary_sum(13, 8)

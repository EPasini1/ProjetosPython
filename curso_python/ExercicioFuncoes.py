def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicador = multiplicar(1,2,3)
print(multiplicador)

def par_impar(numero):
    if numero % 2 == 0:
        return f'{numero} é par'
    return f'{numero} é ímpar'

print(par_impar(multiplicador))
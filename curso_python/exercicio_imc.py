nome = 'Eduardo'
altura = 1.76
peso = 126.5
imc = peso / (altura*altura)

# print(nome, 'tem', altura, 'de altura,')
# print('pesa', peso,'quilos e seu imc é:', imc)


#f-strings
# linha_1 = f'{nome} tem altura de {altura:.2f} de altura,'
# linha_2 = f'pesa {peso} quilos e seu imc é {imc:.2f}'
# print(linha_1)
# print(linha_2)

# #format
# string = '{0} tem {1} de altura, pesa {2} quilos e seu imc é: {3:.2f}'
# formato = string.format(nome, altura, peso, imc)

#format com parâmetro nomeado
string = '{nome} tem {altura} de altura, pesa {peso} quilos e seu imc é: {imc:.2f}'
formato = string.format(nome=nome, altura=altura, peso=peso, imc=imc)

print(formato)
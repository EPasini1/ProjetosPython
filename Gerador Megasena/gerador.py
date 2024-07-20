import pandas as pd
from collections import Counter

# Carregar o arquivo CSV com o separador correto
df = pd.read_csv('mega_sena.csv', sep=';')

# Verificar os nomes das colunas para confirmar
print("Nomes das colunas:", df.columns)

# Ajustar os nomes das colunas conforme exibidos
numeros_colunas = ['bola 1', 'bola 2', 'bola 3', 'bola 4', 'bola 5', 'bola 6']

# Unificar todos os números sorteados em uma única lista
numeros = df[numeros_colunas].values.flatten()

# Contar a frequência de cada número
frequencias = Counter(numeros)

# Ordenar os números pela frequência
numeros_ordenados = [numero for numero, frequencia in frequencias.most_common()]

# Gerar três jogos de 9 números baseados nas frequências
jogo_1 = sorted(numeros_ordenados[:9])
jogo_2 = sorted(numeros_ordenados[9:18])
jogo_3 = sorted(numeros_ordenados[18:27])

# Imprimir os jogos formatados
print("Jogo 1:", ', '.join(map(str, jogo_1)))
print("Jogo 2:", ', '.join(map(str, jogo_2)))
print("Jogo 3:", ', '.join(map(str, jogo_3)))

import pandas as pd
import random
import os

os.chdir('C:\Development\ProjetosPython\Gerador Lotofacil')

# Carregar o arquivo CSV da Lotofácil com o separador correto
df = pd.read_csv('lotofacil.csv', sep=';')

# Verificar os nomes das colunas para confirmar
print("Nomes das colunas:", df.columns)

# Ajustar os nomes das colunas conforme exibidos
numeros_colunas = ['bola 1', 'bola 2', 'bola 3', 'bola 4', 'bola 5', 
                   'bola 6', 'bola 7', 'bola 8', 'bola 9', 'bola 10', 
                   'bola 11', 'bola 12', 'bola 13', 'bola 14', 'bola 15']

# Selecionar apenas os últimos 200 jogos
df_ultimos_200 = df.tail(200)

# Unificar todos os números sorteados dos últimos 200 jogos em uma única lista
numeros = df_ultimos_200[numeros_colunas].values.flatten()

# # Unificar todos os números sorteados em uma única lista
# numeros = df[numeros_colunas].values.flatten()

# Remover duplicatas para obter apenas os números sorteados
numeros_unicos = list(set(numeros))

# Gerar três jogos de 15 números aleatórios
jogo_1 = sorted(random.sample(numeros_unicos, 15))
jogo_2 = sorted(random.sample(numeros_unicos, 15))
jogo_3 = sorted(random.sample(numeros_unicos, 15))
jogo_4 = sorted(random.sample(numeros_unicos, 15))
jogo_5 = sorted(random.sample(numeros_unicos, 15))
jogo_6 = sorted(random.sample(numeros_unicos, 15))

# Imprimir os jogos formatados
print("Jogo 1:", ', '.join(map(str, jogo_1)))
print("Jogo 2:", ', '.join(map(str, jogo_2)))
print("Jogo 3:", ', '.join(map(str, jogo_3)))
print("Jogo 4:", ', '.join(map(str, jogo_4)))
print("Jogo 5:", ', '.join(map(str, jogo_5)))
print("Jogo 6:", ', '.join(map(str, jogo_6)))
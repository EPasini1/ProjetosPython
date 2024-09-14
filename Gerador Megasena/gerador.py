import pandas as pd
import random
from collections import Counter

# Carregar o arquivo CSV com o separador correto
df = pd.read_csv('D:\DevProjects\ProjetosPython\Gerador Megasena\mega_sena.csv', sep=';')

# Verificar os nomes das colunas e ajustar conforme necessário
numeros_colunas = ['bola 1', 'bola 2', 'bola 3', 'bola 4', 'bola 5', 'bola 6']

# Unificar todos os números sorteados em uma única lista e converter para int
numeros = df[numeros_colunas].values.flatten().tolist()
numeros = [int(num) for num in numeros]  # Converte todos para int

# Contar a frequência de cada número
frequencias = Counter(numeros)

# Ordenar os números pela frequência (do menos frequente para o mais frequente)
numeros_ordenados = [numero for numero, frequencia in frequencias.most_common()][::-1]

# Dicas 1 e 2: Evitar números com final 9 ou 0, e evitar certas dezenas que saem pouco
evitar_numeros = [1, 2, 3, 11, 22, 44, 48, 55, 57]
evitar_finais = [9, 0]

# Função para dividir a cartela em quadrantes
def dividir_em_quadrantes():
    quadrante_1 = list(range(1, 16))
    quadrante_2 = list(range(16, 31))
    quadrante_3 = list(range(31, 46))
    quadrante_4 = list(range(46, 61))
    return quadrante_1, quadrante_2, quadrante_3, quadrante_4

# Função para verificar se dois números estão na mesma linha vertical
def mesma_linha_vertical(numero1, numero2):
    return numero1 % 10 == numero2 % 10

# Função para gerar um jogo com base nas dicas fornecidas
def gerar_jogo():
    quadrante_1, quadrante_2, quadrante_3, quadrante_4 = dividir_em_quadrantes()

    jogo = []
    
    # Seleciona 1 número de cada quadrante
    jogo.append(random.choice([n for n in quadrante_1 if n not in evitar_numeros and n % 10 not in evitar_finais]))
    jogo.append(random.choice([n for n in quadrante_2 if n not in evitar_numeros and n % 10 not in evitar_finais]))
    jogo.append(random.choice([n for n in quadrante_3 if n not in evitar_numeros and n % 10 not in evitar_finais]))
    jogo.append(random.choice([n for n in quadrante_4 if n not in evitar_numeros and n % 10 not in evitar_finais]))

    # Preencher os números restantes com base nas frequências e dicas
    while len(jogo) < 7:
        numero = random.choice(numeros_ordenados)
        
        # Verificar se o número respeita as regras
        if (numero not in jogo and 
            numero not in evitar_numeros and 
            numero % 10 not in evitar_finais and 
            not any(abs(numero - n) == 1 for n in jogo) and   # Dica 3: Evitar números seguidos
            not any(mesma_linha_vertical(numero, n) for n in jogo)):  # Dica 4: Não jogar na mesma linha vertical
            
            jogo.append(numero)
    
    # Garantir a presença de números pares e ímpares balanceados (Dica 6)
    pares = [n for n in jogo if n % 2 == 0]
    impares = [n for n in jogo if n % 2 != 0]
    
    if len(pares) > 4:
        jogo.remove(random.choice(pares))
        jogo.append(random.choice([n for n in range(1, 61) if n % 2 != 0 and n not in jogo]))
    elif len(impares) > 4:
        jogo.remove(random.choice(impares))
        jogo.append(random.choice([n for n in range(1, 61) if n % 2 == 0 and n not in jogo]))
    
    return sorted(jogo)

# Função para gerar jogos
def gerar_jogos(n=10):  # Gera 20 jogos de 7 dezenas
    jogos = []
    for _ in range(n):
        jogo = gerar_jogo()
        jogos.append(sorted(jogo))
    return jogos

# Gerar jogos de 7 dezenas
jogos_gerados = gerar_jogos()

# Exibir os jogos gerados
for i, jogo in enumerate(jogos_gerados, 1):
    print(f'Jogo {i}: {jogo}')

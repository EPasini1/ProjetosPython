import pandas as pd
import random
import numpy as np

# Função para calcular a frequência de cada número
def calcular_frequencia(df):
    numeros = df.values.flatten()  # Converter DataFrame em array
    return dict(pd.Series(numeros).value_counts().sort_index())

# Função para determinar números quentes e frios
def numeros_quentes_frios(frequencias, qtd=20):
    ordenado = sorted(frequencias.items(), key=lambda x: x[1], reverse=True)
    quentes = [num for num, _ in ordenado[:qtd]]
    frios = [num for num, _ in ordenado[-qtd:]]
    return quentes, frios

# Gerador de sequência de Fibonacci entre 1 e 60
def gerar_fibonacci():
    a, b = 1, 2
    while a <= 60:
        yield a
        a, b = b, a + b

# Função para gerar um jogo equilibrado
def gerar_jogo_equilibrado(quentes, frios, fibonacci, numeros_por_jogo=6):
    jogo = set()

    # Adicionar números baseando-se em probabilidades
    if len(quentes) >= 3:
        jogo.update(random.sample(quentes, 3))
    if len(frios) >= 2:
        jogo.update(random.sample(frios, 2))

    # Adicionar um número da sequência Fibonacci, se disponível
    fib_disponivel = [num for num in fibonacci if num not in jogo]
    if fib_disponivel:
        jogo.add(random.choice(fib_disponivel))

    # Completar com números aleatórios até atingir o total desejado
    restante = [x for x in range(1, 61) if x not in jogo]
    while len(jogo) < numeros_por_jogo:
        jogo.add(random.choice(restante))

    return sorted(jogo)

# Simulação Monte Carlo para gerar os melhores jogos
def simulacao_monte_carlo(quentes, frios, fibonacci, numeros_por_jogo=6, n_simulacoes=1000, n_jogos=3):
    jogos = set()
    while len(jogos) < n_jogos:
        jogo = tuple(gerar_jogo_equilibrado(quentes, frios, fibonacci, numeros_por_jogo))
        jogos.add(jogo)
    return list(jogos)

# Função principal para gerar jogos
def gerar_jogos(df, numeros_por_jogo=6, n_jogos=3):
    frequencias = calcular_frequencia(df)
    quentes, frios = numeros_quentes_frios(frequencias)
    fibonacci = list(gerar_fibonacci())

    jogos = simulacao_monte_carlo(quentes, frios, fibonacci, numeros_por_jogo, n_simulacoes=1000, n_jogos=n_jogos)
    return jogos

# Leitura do arquivo CSV
def ler_csv(arquivo):
    df = pd.read_csv(arquivo, delimiter=',', encoding='utf-8')
    df.columns = df.columns.str.strip()  # Remove espaços extras dos nomes das colunas
    return df[['bola 1', 'bola 2', 'bola 3', 'bola 4', 'bola 5', 'bola 6']]

# Executar a geração de jogos
if __name__ == "__main__":
    arquivo = 'mega_sena.csv'
    df = ler_csv(arquivo)

    # Configurações iniciais
    numeros_por_jogo = 6
    n_jogos = 1
    jogos = gerar_jogos(df, numeros_por_jogo, n_jogos)

    print("Jogos gerados:")
    for i, jogo in enumerate(jogos, start=1):
        print(f"Jogo {i}: {jogo}")
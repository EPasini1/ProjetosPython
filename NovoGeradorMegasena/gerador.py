import pandas as pd
import random
from collections import Counter

# Função para calcular a frequência de cada número
def calcular_frequencia(df):
    frequencias = {i: 0 for i in range(1, 61)}
    for i in range(len(df)):
        for j in range(0, 6):  # Colunas de índice 0 a 5 (bola 1 a bola 6)
            numero = int(df.iloc[i, j])
            frequencias[numero] += 1
    return frequencias

# Função para determinar números quentes e frios
def numeros_quentes_frios(frequencias):
    quentes = sorted(frequencias, key=frequencias.get, reverse=True)[:20]  # Top 20 mais frequentes
    frios = sorted(frequencias, key=frequencias.get)[:20]  # Top 20 menos frequentes
    return quentes, frios

# Função para gerar números da sequência de Fibonacci entre 1 e 60
def gerar_fibonacci():
    fib = [1, 2]
    while True:
        next_fib = fib[-1] + fib[-2]
        if next_fib > 60:
            break
        fib.append(next_fib)
    return fib

# Função para gerar um jogo equilibrado entre quentes, frios, faixas numéricas e Fibonacci
def gerar_jogo_equilibrado(quentes, frios, fibonacci, numeros_por_jogo):
    # Inicializar o conjunto de números do jogo
    jogo = set()

    # Adicionar 3 números quentes, se disponíveis
    jogo.update(random.sample(quentes, min(3, len(quentes))))

    # Adicionar 3 números frios, se disponíveis
    jogo.update(random.sample(frios, min(3, len(frios))))

    # Adicionar 1 número Fibonacci, se disponível
    fibonacci_disponiveis = [num for num in fibonacci if num not in jogo]
    jogo.update(random.sample(fibonacci_disponiveis, min(1, len(fibonacci_disponiveis))))

    # Adicionar números aleatórios até completar a quantidade desejada
    restante = [x for x in range(1, 61) if x not in jogo]
    if len(jogo) < numeros_por_jogo:
        jogo.update(random.sample(restante, numeros_por_jogo - len(jogo)))

    # Garantir proporção de pares e ímpares (aproximadamente metade de cada)
    pares = [x for x in jogo if x % 2 == 0]
    impares = [x for x in jogo if x % 2 != 0]

    while len(pares) < numeros_por_jogo // 2 and len(jogo) < numeros_por_jogo:
        par_extra = random.choice([x for x in restante if x % 2 == 0 and x not in jogo])
        jogo.add(par_extra)
        restante.remove(par_extra)
        pares = [x for x in jogo if x % 2 == 0]

    while len(impares) < numeros_por_jogo // 2 and len(jogo) < numeros_por_jogo:
        impar_extra = random.choice([x for x in restante if x % 2 != 0 and x not in jogo])
        jogo.add(impar_extra)
        restante.remove(impar_extra)
        impares = [x for x in jogo if x % 2 != 0]

    # Manter a quantidade desejada de números no jogo
    return sorted(jogo)

# Função para criar jogos usando simulação de Monte Carlo
def simulacao_monte_carlo(frequencias, quentes, frios, fibonacci, numeros_por_jogo, n_simulacoes=1000, n_jogos=6):
    melhores_jogos = []
    for _ in range(n_simulacoes):
        jogo = gerar_jogo_equilibrado(quentes, frios, fibonacci, numeros_por_jogo)
        if validar_jogo(jogo, numeros_por_jogo):
            melhores_jogos.append(jogo)
        if len(melhores_jogos) >= n_jogos:
            break
    return melhores_jogos[:n_jogos]  # Retornar n_jogos melhores jogos

# Função para validar jogo baseado em regras de pares, ímpares e faixas
def validar_jogo(jogo, numeros_por_jogo):
    # Proporção de pares e ímpares
    pares = len([x for x in jogo if x % 2 == 0])
    impares = len([x for x in jogo if x % 2 != 0])

    # Análise de faixas numéricas (1-10, 11-20, etc.)
    faixas = [0] * 6
    for num in jogo:
        faixas[(num - 1) // 10] += 1

    # Regras: proporção de pares e ímpares e pelo menos 1 número de diferentes faixas
    return (pares in [numeros_por_jogo // 2, numeros_por_jogo // 2 + 1] and
            impares in [numeros_por_jogo // 2, numeros_por_jogo // 2 + 1] and
            sum(1 for x in faixas if x > 0) >= 3)

# Função principal para gerar jogos
def gerar_jogos(df, numeros_por_jogo=10, n_jogos=6):
    frequencias = calcular_frequencia(df)
    quentes, frios = numeros_quentes_frios(frequencias)
    fibonacci = gerar_fibonacci()

    # Usar Monte Carlo para gerar os melhores jogos
    jogos = simulacao_monte_carlo(frequencias, quentes, frios, fibonacci, numeros_por_jogo, n_simulacoes=1000, n_jogos=n_jogos)

    return jogos[:n_jogos]

# Leitura do arquivo CSV
def ler_csv(arquivo):
    df = pd.read_csv(arquivo, delimiter=';', usecols=['bola 1', 'bola 2', 'bola 3', 'bola 4', 'bola 5', 'bola 6'])
    return df

# Executar a geração de jogos
if __name__ == "__main__":
    arquivo = 'mega_sena.csv'
    df = ler_csv(arquivo)
    
    # Configurações iniciais
    numeros_por_jogo = 7  # Quantidade de números em cada jogo
    n_jogos = 10  # Quantidade de jogos a serem gerados
    
    jogos = gerar_jogos(df, numeros_por_jogo, n_jogos)

    print("Jogos gerados:")
    for i, jogo in enumerate(jogos, start=1):
        print(f"Jogo {i}: {jogo}")

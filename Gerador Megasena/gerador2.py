import csv
import random

# Função para carregar os números mais frequentes da Mega-Sena a partir do arquivo .csv
def carregar_numeros_mais_frequentes(arquivo_csv):
    frequencia_numeros = {}
    with open(arquivo_csv, mode='r') as file:
        reader = csv.reader(file, delimiter=';')  # Usar ; como delimitador
        next(reader)  # Pular o cabeçalho
        for row in reader:
            try:
                numero = int(row[2])  # Assumindo que o número da Mega-Sena está na 3ª coluna
                frequencia_numeros[numero] = frequencia_numeros.get(numero, 0) + 1
            except ValueError:
                print(f"Erro ao converter {row} para número. Verifique o formato.")
    return frequencia_numeros

# Função para dividir a cartela em quadrantes
def dividir_em_quadrantes():
    quadrante_1 = list(range(1, 16))
    quadrante_2 = list(range(16, 31))
    quadrante_3 = list(range(31, 46))
    quadrante_4 = list(range(46, 61))
    return quadrante_1, quadrante_2, quadrante_3, quadrante_4

# Função para gerar um jogo com base nas dicas fornecidas
def gerar_jogo(frequencia_numeros):
    quadrante_1, quadrante_2, quadrante_3, quadrante_4 = dividir_em_quadrantes()

    jogo = []
    
    # Seleciona 1 número de cada quadrante
    jogo.append(random.choice(quadrante_1))
    jogo.append(random.choice(quadrante_2))
    jogo.append(random.choice(quadrante_3))
    jogo.append(random.choice(quadrante_4))

    # Garantir a presença de números espaçados
    while len(jogo) < 6:
        numero = random.randint(1, 60)
        # Evitar números consecutivos
        if not any(abs(numero - n) == 1 for n in jogo):
            jogo.append(numero)
    
    # Balancear pares e ímpares
    pares = [n for n in jogo if n % 2 == 0]
    impares = [n for n in jogo if n % 2 != 0]
    
    if len(pares) > 4:
        jogo.remove(random.choice(pares))
        jogo.append(random.choice([n for n in range(1, 61) if n % 2 != 0 and n not in jogo]))
    elif len(impares) > 4:
        jogo.remove(random.choice(impares))
        jogo.append(random.choice([n for n in range(1, 61) if n % 2 == 0 and n not in jogo]))
    
    return sorted(jogo)

# Função para gerar 10 jogos
def gerar_jogos(frequencia_numeros, n=3):
    jogos = []
    for _ in range(n):
        jogo = gerar_jogo(frequencia_numeros)
        jogos.append(jogo)
    return jogos

# Carregar os números mais frequentes da Mega-Sena
frequencia_numeros = carregar_numeros_mais_frequentes('D:\\DevProjects\\ProjetosPython\\Gerador Megasena\\mega_sena.csv')

# Gerar 10 jogos
jogos_gerados = gerar_jogos(frequencia_numeros)

# Exibir os jogos gerados
for i, jogo in enumerate(jogos_gerados, 1):
    print(f'Jogo {i}: {jogo}')

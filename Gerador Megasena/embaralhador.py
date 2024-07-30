import random

def embaralhar_jogos(jogos):
    # Verificar se cada jogo tem 9 números únicos
    for jogo in jogos:
        if len(jogo) != 9 or len(set(jogo)) != 9:
            raise ValueError("Cada jogo deve conter 9 números únicos.")
    
    # Unir todos os números em uma única lista
    todos_numeros = [numero for jogo in jogos for numero in jogo]
    
    # Embaralhar todos os números
    random.shuffle(todos_numeros)
    
    # Formar 3 novos jogos, cada um com 6 números
    novos_jogos = []
    for i in range(3):
        novo_jogo = sorted(todos_numeros[i*9:(i+1)*9])
        novos_jogos.append(novo_jogo)
    
    return novos_jogos

# Exemplo de uso
jogos = [
    [1, 5, 8, 21, 29, 36, 39, 49, 51],
    [3, 14, 22, 31, 37, 38, 40, 54, 59],
    [12, 15, 18, 28, 41, 50, 55, 58, 60],
    [4, 9, 13, 17, 26, 30, 35, 56, 57],
    [6, 7, 10, 16, 34, 43, 44, 52, 53],
    [11, 19, 20, 25, 27, 42, 45, 46, 47]
]

novos_jogos = embaralhar_jogos(jogos)
print("Novos jogos formados:")
for jogo in novos_jogos:
    print(jogo)

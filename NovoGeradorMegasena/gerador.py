import pandas as pd
import random
<<<<<<< HEAD
from collections import Counter
import sys # Import sys for error messages

# --- Constants ---
MIN_NUMBER = 1
MAX_NUMBER = 60
NUMBERS_PER_MEGA_SENA_GAME = 6 # The standard Mega Sena game size
TOP_N_FREQUENT = 20 # Number of 'hot' numbers
TOP_N_INFREQUENT = 20 # Number of 'cold' numbers
# Desired composition (can be made configurable)
HOT_COUNT = 3
COLD_COUNT = 3
FIBONACCI_COUNT = 1
MIN_RANGE_COUNT = 3 # Minimum number of ranges (1-10, 11-20, etc.) a game should span

# --- Functions ---

def ler_csv(arquivo: str) -> pd.DataFrame | None:
    """
    Lê o arquivo CSV contendo os resultados da Mega Sena.

    Args:
        arquivo: O caminho para o arquivo CSV.

    Returns:
        Um DataFrame pandas com as colunas das bolas, ou None se houver erro.
    """
    try:
        df = pd.read_csv(arquivo, delimiter=';', usecols=['bola 1', 'bola 2', 'bola 3', 'bola 4', 'bola 5', 'bola 6'])
        # Convertendo as colunas para tipo numérico, tratando possíveis erros
        for col in ['bola 1', 'bola 2', 'bola 3', 'bola 4', 'bola 5', 'bola 6']:
             df[col] = pd.to_numeric(df[col], errors='coerce')
        # Remover linhas onde a conversão falhou (valores NaN)
        df.dropna(subset=['bola 1', 'bola 2', 'bola 3', 'bola 4', 'bola 5', 'bola 6'], inplace=True)
        return df
    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo}' não encontrado.", file=sys.stderr)
        return None
    except KeyError:
        print(f"Erro: O arquivo '{arquivo}' não contém as colunas esperadas ('bola 1' a 'bola 6').", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Erro ao ler o arquivo CSV: {e}", file=sys.stderr)
        return None

def calcular_frequencia(df: pd.DataFrame) -> Counter[int]:
    """
    Calcula a frequência de cada número nos resultados históricos.

    Args:
        df: DataFrame pandas com os resultados.

    Returns:
        Um objeto Counter onde as chaves são os números (1-60) e os valores são suas frequências.
    """
    all_numbers = []
    # Itera sobre as colunas de 'bola' e adiciona os números a uma lista
    for col in ['bola 1', 'bola 2', 'bola 3', 'bola 4', 'bola 5', 'bola 6']:
        # Usar extend é mais eficiente do que append em um loop
        all_numbers.extend(df[col].tolist())

    # Usa Counter para calcular as frequências
    # Filtra para garantir que apenas números dentro do intervalo [MIN_NUMBER, MAX_NUMBER] são contados
    frequencias = Counter(num for num in all_numbers if MIN_NUMBER <= num <= MAX_NUMBER)

    # Garantir que todos os números de 1 a 60 estejam no Counter, mesmo que com frequência 0
    for i in range(MIN_NUMBER, MAX_NUMBER + 1):
        if i not in frequencias:
            frequencias[i] = 0

    return frequencias

def numeros_quentes_frios(frequencias: Counter[int]) -> tuple[list[int], list[int]]:
    """
    Determina os números mais frequentes (quentes) e menos frequentes (frios).

    Args:
        frequencias: Um Counter com a frequência de cada número.

    Returns:
        Uma tupla contendo duas listas: uma com os números quentes e outra com os números frios.
    """
    # Ordena os itens do Counter pela frequência
    sorted_by_frequency = sorted(frequencias.items(), key=lambda item: item[1])

    # Os primeiros TOP_N_INFREQUENT são os mais frios
    frios = [num for num, freq in sorted_by_frequency[:TOP_N_INFREQUENT]]

    # Os últimos TOP_N_FREQUENT são os mais quentes
    # Usa [::-1] para reverter a lista já ordenada ascendentemente por frequência
    quentes = [num for num, freq in sorted_by_frequency[-TOP_N_FREQUENT:][::-1]]

    return quentes, frios

def gerar_fibonacci() -> list[int]:
    """
    Gera números da sequência de Fibonacci dentro do intervalo [MIN_NUMBER, MAX_NUMBER].

    Returns:
        Uma lista de números Fibonacci entre MIN_NUMBER e MAX_NUMBER.
    """
    fib = [1, 2]
    # Ajusta o início se MIN_NUMBER > 1
    if MIN_NUMBER > 1:
         fib = [f for f in fib if f >= MIN_NUMBER]

    while True:
        next_fib = fib[-1] + fib[-2]
        if next_fib > MAX_NUMBER:
            break
        if next_fib >= MIN_NUMBER: # Garantir que o número gerado está dentro do range
            fib.append(next_fib)
        else: # Se next_fib ainda for menor que MIN_NUMBER, continua gerando
            pass # Não adiciona, mas o loop continuará

    return fib

def gerar_jogo_equilibrado(quentes: list[int], frios: list[int], fibonacci: list[int], numeros_por_jogo: int) -> list[int]:
    """
    Gera um jogo tentando equilibrar números quentes, frios, Fibonacci e aleatórios.

    Note: This function generates a *candidate* game based on a strategy.
    Validation (`validar_jogo`) or further balancing might be needed afterwards,
    depending on the desired strictness.

    Args:
        quentes: Lista de números quentes.
        frios: Lista de números frios.
        fibonacci: Lista de números Fibonacci.
        numeros_por_jogo: Quantidade de números no jogo final.

    Returns:
        Uma lista sorted com os números do jogo gerado.
    """
=======
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
>>>>>>> 54e2e036ecc9b6f5a8f831d9f3cb1871a07ca4fd
    jogo = set()
    pool_completo = set(range(MIN_NUMBER, MAX_NUMBER + 1))

<<<<<<< HEAD
    # Adicionar números quentes
    # Usa min() para não tentar pegar mais números do que disponíveis
    num_quentes_a_adicionar = min(HOT_COUNT, len(quentes))
    jogo.update(random.sample(quentes, num_quentes_a_adicionar))

    # Adicionar números frios
    # Garante que os frios não sejam duplicados (já no jogo)
    frios_disponiveis = list(set(frios) - jogo)
    num_frios_a_adicionar = min(COLD_COUNT, len(frios_disponiveis))
    jogo.update(random.sample(frios_disponiveis, num_frios_a_adicionar))

    # Adicionar números Fibonacci
    # Garante que os fibonacci não sejam duplicados (já no jogo)
    fibonacci_disponiveis = list(set(fibonacci) - jogo)
    num_fibonacci_a_adicionar = min(FIBONACCI_COUNT, len(fibonacci_disponiveis))
    jogo.update(random.sample(fibonacci_disponiveis, num_fibonacci_a_adicionar))

    # Preencher o restante com números aleatórios do pool disponível
    # Cria um pool de números que ainda não estão no jogo
    restante_pool = list(pool_completo - jogo)
    num_restante_a_adicionar = numeros_por_jogo - len(jogo)

    if num_restante_a_adicionar > 0 and len(restante_pool) >= num_restante_a_adicionar:
         jogo.update(random.sample(restante_pool, num_restante_a_adicionar))
    elif num_restante_a_adicionar > 0:
        # Caso raro onde não há números suficientes restantes, mas o set já deve ter sido preenchido
        # ou houve um erro lógico anterior. Adiciona o máximo possível.
        jogo.update(random.sample(restante_pool, len(restante_pool)))


    # --- Melhoria Sugerida: Refinar o balanceamento de pares/ímpares e faixas AQUI ---
    # Em vez de adicionar/remover de forma complexa, você poderia:
    # 1. Contar quantos pares/ímpares e faixas o jogo ATUAL possui.
    # 2. Identificar quantos de cada tipo (par/ímpar, faixa) ainda são necessários para a meta desejada.
    # 3. Tentar substituir ou adicionar números do pool restante que ajudem a atingir essas metas,
    #    dando preferência a manter quentes/frios/fibonacci já selecionados.
    # Exemplo (conceitual):
    # current_pares = len([x for x in jogo if x % 2 == 0])
    # needed_pares = (numeros_por_jogo // 2) - current_pares
    # if needed_pares > 0:
    #    pool_pares = [x for x in restante_pool if x % 2 == 0]
    #    # Tentar adicionar needed_pares a partir de pool_pares sem exceder numeros_por_jogo
    # if needed_pares < 0: # Temos pares demais
    #    # Tentar substituir abs(needed_pares) pares por ímpares do pool restante
    # Similar logic for odd and ranges.

    # A lógica original de balanço de pares/ímpares ao final é ineficiente e pode distorcer
    # as escolhas de quentes/frios/fibonacci feitas antes.
    # Se a validação de par/ímpar e faixas for CRÍTICA, é melhor refinar a GERAÇÃO
    # neste ponto para atingir a meta, ou depender mais fortemente da função validar_jogo
    # e da simulação de Monte Carlo para filtrar.

    # A lógica original de "pop" se o jogo for maior que numeros_por_jogo é perigosa,
    # pois remove elementos aleatoriamente. Melhor garantir que não exceda durante a adição.
    # Como estamos usando set.update e random.sample com tamanhos calculados, isso deve ser evitado.

    # Garante o tamanho final (embora a lógica de adição acima deva garantir isso)
    # Se por algum motivo o jogo ficou maior (o que não deveria acontecer com a lógica acima)
    while len(jogo) > numeros_por_jogo:
         # remove um elemento aleatório, menos ideal do que garantir o tamanho antes
         jogo.pop()
    # Se ficou menor, o que pode acontecer se o pool restante não for suficiente
    # (extremamente improvável com 1-60 e numeros_por_jogo=6), ele simplesmente retorna menor.
    # A simulação Monte Carlo pode filtrar jogos de tamanho incorreto se a validação incluir o tamanho.


    return sorted(list(jogo))

def validar_jogo(jogo: list[int], numeros_por_jogo: int) -> bool:
    """
    Valida um jogo gerado com base em regras de pares, ímpares e faixas numéricas.

    Args:
        jogo: A lista de números do jogo gerado.
        numeros_por_jogo: O tamanho esperado do jogo.

    Returns:
        True se o jogo for válido, False caso contrário.
    """
    if len(jogo) != numeros_por_jogo:
        return False # Jogo não tem o tamanho correto

    pares = len([x for x in jogo if x % 2 == 0])
    impares = len([x for x in jogo if x % 2 != 0])

    # Regra 1: Proporção de pares e ímpares (aproximadamente metade de cada)
    # Permite uma variação de +/- 1
    is_even_odd_balanced = (pares >= numeros_por_jogo // 2 - 1 and
                            pares <= numeros_por_jogo // 2 + 1 and
                            impares >= numeros_por_jogo // 2 - 1 and
                            impares <= numeros_por_jogo // 2 + 1)
    # Para numeros_por_jogo=6, isso significa 2, 3 ou 4 pares E 2, 3 ou 4 ímpares.
    # O mais comum e recomendado é 3 pares e 3 ímpares. A validação original era mais restritiva.
    # Vamos manter a validação original que aceita apenas //2 ou //2 + 1 para ser fiel ao código base.
    is_even_odd_balanced_strict = (pares in [numeros_por_jogo // 2, numeros_por_jogo // 2 + 1] and
                                   impares in [numeros_por_jogo // 2, numeros_por_jogo // 2 + 1])


    # Regra 2: Análise de faixas numéricas (1-10, 11-20, etc.)
    faixas_count = [0] * ((MAX_NUMBER // 10) + (1 if MAX_NUMBER % 10 != 0 else 0)) # Calcula o número de faixas
    for num in jogo:
         if MIN_NUMBER <= num <= MAX_NUMBER: # Garantir que o número está no range válido
            faixas_count[(num - MIN_NUMBER) // 10] += 1

    # Conta quantas faixas têm pelo menos 1 número
    num_faixas_com_numeros = sum(1 for count in faixas_count if count > 0)

    # Regra 2: Pelo menos MIN_RANGE_COUNT faixas diferentes devem ter números
    is_range_covered = num_faixas_com_numeros >= MIN_RANGE_COUNT

    # O jogo é válido se ambas as regras forem atendidas
    return is_even_odd_balanced_strict and is_range_covered


def simulacao_monte_carlo(frequencias: Counter[int], quentes: list[int], frios: list[int], fibonacci: list[int], numeros_por_jogo: int, n_simulacoes: int = 1000, n_jogos: int = 6) -> list[list[int]]:
    """
    Gera jogos usando simulação, validando cada um.

    Args:
        frequencias: Frequências históricas.
        quentes: Lista de números quentes.
        frios: Lista de números frios.
        fibonacci: Lista de números Fibonacci.
        numeros_por_jogo: Quantidade de números por jogo.
        n_simulacoes: Número máximo de simulações a rodar.
        n_jogos: Número de jogos válidos a tentar encontrar.

    Returns:
        Uma lista contendo n_jogos listas de números válidos.
    """
    melhores_jogos: list[list[int]] = []
    for _ in range(n_simulacoes):
        jogo = gerar_jogo_equilibrado(quentes, frios, fibonacci, numeros_por_jogo)
        # Note: A validação agora inclui a verificação do tamanho do jogo
        if validar_jogo(jogo, numeros_por_jogo):
            # Adiciona o jogo apenas se ele ainda não estiver na lista (evita duplicatas)
            if jogo not in melhores_jogos:
                 melhores_jogos.append(jogo)

        # Para a simulação assim que encontrar o número desejado de jogos
        if len(melhores_jogos) >= n_jogos:
            break

    # Retorna o número desejado de jogos (ou menos, se não encontrou o suficiente)
    return melhores_jogos[:n_jogos]

def gerar_jogos(df: pd.DataFrame, numeros_por_jogo: int = NUMBERS_PER_MEGA_SENA_GAME, n_jogos: int = 6) -> list[list[int]]:
    """
    Função principal para analisar os dados e gerar jogos.

    Args:
        df: DataFrame pandas com os resultados históricos.
        numeros_por_jogo: Quantidade de números em cada jogo gerado.
        n_jogos: Quantidade de jogos a serem gerados.

    Returns:
        Uma lista contendo os jogos gerados.
    """
    if numeros_por_jogo < NUMBERS_PER_MEGA_SENA_GAME or numeros_por_jogo > MAX_NUMBER:
        print(f"Erro: O número de números por jogo ({numeros_por_jogo}) deve ser entre {NUMBERS_PER_MEGA_SENA_GAME} e {MAX_NUMBER}.", file=sys.stderr)
        return []

    if n_jogos <= 0:
        print("Erro: A quantidade de jogos a gerar deve ser positiva.", file=sys.stderr)
        return []

=======
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
>>>>>>> 54e2e036ecc9b6f5a8f831d9f3cb1871a07ca4fd
    frequencias = calcular_frequencia(df)
    quentes, frios = numeros_quentes_frios(frequencias)
    fibonacci = list(gerar_fibonacci())

<<<<<<< HEAD
    # Usar Monte Carlo para gerar os melhores jogos (filtrando pelos critérios de validação)
    jogos = simulacao_monte_carlo(frequencias, quentes, frios, fibonacci, numeros_por_jogo,
                                  n_simulacoes=5000, # Aumenta o número de simulações para ter mais chances de encontrar jogos válidos
                                  n_jogos=n_jogos)

    return jogos

# --- Execução Principal ---
if __name__ == "__main__":
    arquivo_csv = 'mega_sena.csv' # Nome do arquivo CSV
    df_resultados = ler_csv(arquivo_csv)

    if df_resultados is not None:
        # Configurações para esta execução específica
        numeros_do_jogo = NUMBERS_PER_MEGA_SENA_GAME # Gera jogos de 6 números (padrão da Mega Sena)
        quantidade_de_jogos = 3 # Gera 3 jogos

        jogos_gerados = gerar_jogos(df_resultados, numeros_do_jogo, quantidade_de_jogos)

        if jogos_gerados:
            print("\n--- Jogos Gerados para a Mega Sena ---")
            for i, jogo in enumerate(jogos_gerados, start=1):
                print(f"Jogo {i}: {sorted(jogo)}") # Garante que a saída esteja sempre ordenada
            print("--------------------------------------")
        else:
             print("\nNão foi possível gerar jogos válidos com os critérios definidos.")
=======
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
>>>>>>> 54e2e036ecc9b6f5a8f831d9f3cb1871a07ca4fd

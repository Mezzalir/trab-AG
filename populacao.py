"""
populacao.py

Criação dos indivíduos e da população inicial do Algoritmo Genético.

codificar(numero): converte um número inteiro entre -15 e 15 em 5 bits
(sinal-magnitude). Primeiro define o bit de sinal: 1 se o número for
negativo e 0 se for positivo ou zero. Depois pega o valor absoluto
(magnitude) e o converte para binário com 4 dígitos, completando com
zeros à esquerda. Por fim, junta o bit de sinal com os 4 bits da
magnitude e devolve um array numpy.
Exemplos: -3 -> [1 0 0 1 1] | 15 -> [0 1 1 1 1]

criar_individuo(rng): sorteia x e y inteiros entre -15 e 15, codifica
cada um em 5 bits e junta os dois num array de 10 bits [x | y].
"""

import numpy as np

LIMITE = 15  # domínio: inteiros de -LIMITE a +LIMITE


def codificar(numero):
    """Converte um número inteiro de -15 a 15 em 5 bits (sinal-magnitude)."""

    if numero < 0:
        sinal = 1
    else:
        sinal = 0

    # valor absoluto, sem sinal!
    magnitude = abs(numero)

    # magnitude em binário com 4 dígitos
    binario = format(magnitude, "04b")

    # junta o sinal com os 4 bits de magnitude
    bits = [sinal] + [int(b) for b in binario]

    # converte a lista em array numpy de inteiros
    return np.array(bits, dtype=int)


def criar_individuo(rng):
    """Cria um indivíduo aleatório: sorteia x e y e junta os bits (10 bits)."""

    # sorteia x e y em [-15, 15]; o high do integers NÃO é incluído, por isso LIMITE + 1 [-15, +15)
    x = rng.integers(-LIMITE, LIMITE + 1)
    y = rng.integers(-LIMITE, LIMITE + 1)

    # codifica x e y e concatena os dois arrays num único array de 10 bits
    return np.concatenate([codificar(x), codificar(y)])

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
"""

import numpy as np


def codificar(numero):
    "Converte um número inteiro de -15, +15  em 5 bits (sinal magnitude"

    if numero < 0:
        sinal = 1
    else:
        sinal = 0

    # valor absoluto, sem sinal!
    magnitude = abs(numero)

    # magnitude em  binário com 4 dígitos.
    binario = format(magnitude, "04b")

    #  Junta o sinal com os 4 bits de magnitude
    bits = [sinal] + [int(b) for b in binario]

    # Retorno e  converte a lista em array numpy de inteiros
    return np.array(bits, dtype=int)


# testes: só rodam com "python populacao.py", são ignorados quando o arquivo é importado
if __name__ == "__main__":
    for n in [5, -5, 0, 15, -15, -8]:
        print(n, codificar(n))

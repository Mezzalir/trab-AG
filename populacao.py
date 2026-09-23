
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


def criar_populacao(tamanho, rng):
    """Cria a população inicial: matriz (tamanho, 10), um indivíduo por linha."""

    individuos = []

    for i in range(tamanho):
        individuo = criar_individuo(rng)

        individuos.append(individuo)

    # transforma a lista de indivíduos numa matriz: cada indivíduo vira uma linha
    return np.array(individuos)

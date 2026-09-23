import random


def codificar(numero):
    # bit de sinal: 1 se for negativo, 0 se for positivo ou zero
    if numero < 0:
        sinal = 1
    else:
        sinal = 0

    # valor absoluto, sem sinal
    magnitude = abs(numero)

    # magnitude em binário com 4 dígitos, como texto
    binario = format(magnitude, "04b")

    # começa a lista com o bit de sinal
    bits = [sinal]

    # acrescenta cada dígito do binário, convertido para número
    for digito in binario:
        bits.append(int(digito))

    return bits


def criar_individuo():
    # sorteia x e y entre -15 e 15
    x = random.randint(-15, 15)
    y = random.randint(-15, 15)

    # junta os 5 bits de x com os 5 bits de y
    individuo = codificar(x) + codificar(y)

    return individuo


def criar_populacao(tamanho):
    # listas de listas
    populacao = []

    for i in range(tamanho):
        individuo = criar_individuo()
        populacao.append(individuo)

    return populacao

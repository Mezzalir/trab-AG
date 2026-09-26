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


def decodificar(bits):

    num = 0
    i = 4
    p = 0

    while i >= 1:
        num += int(bits[i]) * (2**p)
        p += 1
        i -= 1

    if bits[0] == 1:
        num *= -1

    return num

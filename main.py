import populacao

# visualizacao basica da primeira geracao do ag funcionando :

tamMaxPop = int(input("Digite o numero maximo da populacao: "))

# criando nossa primeira populacao
populacao_inicial = populacao.Populacao()

# tamanho da populacao inical definido pelo usuario
populacao_inicial.criar_populacao(tamMaxPop)

print("Populacao inicial:")
populacao_inicial.imprimir_populacao()

print("\nPopulacao inicial ordenada:")
populacao_inicial.ordenar_populacao()
populacao_inicial.imprimir_populacao()

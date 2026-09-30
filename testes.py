import populacao as p

print("Testando o funcionamento das funcoes...\n")

populacao = p.Populacao()

# Cria populacao inicial
populacao.criar_populacao(6)

print("Nossa populacao inicial:")
populacao.imprimir_populacao()
print()

print("Nossa populacao inicial ordenada:")
populacao.ordenar_populacao()
populacao.imprimir_populacao()
print()

print("Atribuindo rank e probabilidades ao individuo")
populacao.atribuir_ranking()
populacao.calcular_probabilidades()
populacao.imprimir_populacao()
print()

print("Vamos conhecer nossa pool de acasalamento")
populacao.selecionar_pais()
populacao.imprimir_pool()
print()

print("Vamos conhecer nossa pool de acasalamento ordenada")
populacao.imprimir_pool()
print()

print("Quem eh o elite da populacao")
elite = populacao.aplicar_elitismo()
print(f"Elite = {elite.genes} fitness {elite.fitness}")
print(f"Elite passa pra nova geracao direto sem crossover")
print()


print("Testando o crossover + mutacao")
populacao.cruzamento()

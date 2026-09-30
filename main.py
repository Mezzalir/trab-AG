import populacao as p

tamanho = int(input("Tamanho da populacao: "))
geracoes = int(input("Numero de geracoes: "))
taxa_cruzamento = float(input("Taxa de cruzamento (0 a 1): "))
taxa_mutacao = float(input("Taxa de mutacao (0 a 1): "))

populacao = p.Populacao()
populacao.num_geracoes = geracoes
populacao.taxa_cruzamento = taxa_cruzamento
populacao.taxa_mutacao = taxa_mutacao
populacao.criar_populacao(tamanho)
populacao.gerar_geracoes()
populacao.salvar_log_em_arquivo("log.csv")

import populacao as p
import graficos

tamanho = int(input("Tamanho da populacao: "))
n_geracoes = int(input("Numero de geracoes: "))
taxa_cruzamento = float(input("Taxa de cruzamento (0 a 1): "))
taxa_mutacao = float(input("Taxa de mutacao (0 a 1): "))

populacao = p.Populacao(tamanho, n_geracoes, taxa_mutacao, taxa_cruzamento)
populacao.num_geracoes = n_geracoes
populacao.taxa_cruzamento = taxa_cruzamento
populacao.taxa_mutacao = taxa_mutacao
populacao.criar_populacao()
populacao.gerar_geracoes()
populacao.salvar_log_em_arquivo("log.csv")
graficos.plotar_fitness_medio(populacao.historico)

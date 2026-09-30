import populacao as p

populacao = p.Populacao()
populacao.criar_populacao(200)
populacao.gerar_geracoes()
populacao.salvar_log_em_arquivo("log.csv")

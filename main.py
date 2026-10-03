import populacao as p
import graficos

def saudacoes():
    print("================= Algoritmo Genético ===========================")
    print("\nAutores: Lucas William Mezzalira")
    print("         Pedro Paulo Rockenbach")
    print("\nDigite os parâmetros do algoritmo:")

def footer(geracoes):
    print(f"\nAlgoritmo executado com sucesso nas {geracoes} gerações!\n")
    print("Para avaliar os gráficos solicitados, consulte a pasta imagens/")
    print("Para avaliar o log, entre na pasta logs/\n")
    print("================================================================")

saudacoes()

tamanho = int(input("Tamanho da população (ex: 200): "))
n_geracoes = int(input("Número de gerações (ex : 50): "))
taxa_cruzamento = float(input("Taxa de cruzamento (0 a 1) (ex: 0.7): "))
taxa_mutacao = float(input("Taxa de mutação (0 a 1) (ex: 0.01): "))


populacao = p.Populacao(tamanho, n_geracoes, taxa_mutacao, taxa_cruzamento)
populacao.num_geracoes = n_geracoes
populacao.taxa_cruzamento = taxa_cruzamento
populacao.taxa_mutacao = taxa_mutacao
populacao.criar_populacao()
populacao.gerar_geracoes()
populacao.salvar_log_em_arquivo("log.csv")
graficos.plotar_fitness_medio(populacao.historico)

footer(n_geracoes)

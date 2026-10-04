import graficos
import populacao as p
import itertools
import threading
import time
import sys

def saudacoes():
    print("================= Algoritmo Genético ===========================")
    print("\nAutores: Lucas Willian Mezzalira")
    print("         Pedro Paulo Rockenbach")
    print("\nDigite os parâmetros do algoritmo:")


def footer(geracoes, pasta):
    print(f"\nAlgoritmo executado com sucesso nas {geracoes} gerações!\n")
    print(f"- Para avaliar os gráficos desta execução, consulte a pasta {pasta}/")
    print("- Para avaliar o log, entre na pasta logs/\n")
    print("================================================================")


saudacoes()

tamanho = int(input("Tamanho da população (ex: 200): "))
n_geracoes = int(input("Número de gerações (ex : 50): "))
taxa_cruzamento = float(input("Taxa de cruzamento (0 a 1) (ex: 0.7): "))
taxa_mutacao = float(input("Taxa de mutação (0 a 1) (ex: 0.01): "))
print()

done = False

def animate():
    for c in itertools.cycle(["|", "/", "-", "\\"]):
        if done:
            break
        sys.stdout.write("\rAlgoritmo evoluindo  " + c)
        sys.stdout.flush()
        time.sleep(0.1)

t = threading.Thread(target=animate, daemon=True)
t.start()

populacao = p.Populacao(tamanho, n_geracoes, taxa_mutacao, taxa_cruzamento)
populacao.num_geracoes = n_geracoes
populacao.taxa_cruzamento = taxa_cruzamento
populacao.taxa_mutacao = taxa_mutacao
populacao.criar_populacao()
populacao.gerar_geracoes()
populacao.salvar_log_em_arquivo("log.csv")

pasta = graficos.criar_pasta_execucao()
grafico = graficos.GraficoPopulacao(populacao.historico, pasta)
grafico.plotar_grafico_comportamento()
graficos.plotar_fitness_medio(populacao.historico, pasta)

done = True

footer(n_geracoes, pasta)

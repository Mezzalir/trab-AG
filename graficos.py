import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from code_e_decode import codificar, decodificar


class GraficoPopulacao:
    def __init__(self, populacao, geracao):
        self.populacao = populacao
        self.g = geracao

    def plotar_grafico_comportamento(self):

        x0 = []
        y0 = []

        for i in self.populacao:
            x0.append(decodificar(i.genes))
            y0.append(decodificar(i.genes))

        x = np.array(x0)
        y = np.array(x0)

        plt.scatter(x, y)
        plt.title(f"Comportamento da população na Geração {self.g}")
        plt.xlabel("Valor de X")
        plt.ylabel("Valor de Y")
        plt.savefig("imagens/grafico_geracao.png", dpi=300, bbox_inches="tight")


def plotar_fitness_medio(historico):
    geracoes = []
    medias = []

    for g in historico:
        # eixo x
        geracoes.append(g.geracao)
        # eixo y
        medias.append(g.media)

    plt.figure()
    plt.plot(geracoes, medias)
    plt.title("Fitness médio por geracao")
    plt.xlabel("Geracao")
    plt.ylabel("Fitness médio")
    plt.savefig("imagens/fitness_medio.png", dpi=300, bbox_inches="tight")
    plt.close()

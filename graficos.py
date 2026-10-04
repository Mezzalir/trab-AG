import matplotlib

matplotlib.use("Agg")
import os

import matplotlib.pyplot as plt

from code_e_decode import codificar, decodificar


def criar_pasta_execucao():

    os.makedirs("graficos", exist_ok=True)

    numero_execucao = 1

    while os.path.exists(f"graficos/execucao_{numero_execucao}"):
        numero_execucao = numero_execucao + 1

    pasta = f"graficos/execucao_{numero_execucao}"

    os.makedirs(pasta + "/populacao")

    return pasta


class GraficoPopulacao:

    def __init__(self, historico, pasta):
        self.historico = historico
        self.pasta = pasta

    def plotar_grafico_comportamento(self):

        for g in self.historico:

            x = []
            y = []

            for ponto in g.pontos:
                x.append(ponto[0])
                y.append(ponto[1])

            plt.figure(figsize=(8, 6))

            plt.scatter(x, y, color="blue", label="População")

            plt.scatter(g.melhor_x, g.melhor_y, color="red", marker="*",
                s=250, label="Melhor indivíduo")

            plt.xlabel("X")
            plt.ylabel("Y")

            plt.xlim(-16, 16)
            plt.ylim(-16, 16)

            plt.title(f"Comportamento da população - " f"Geração {g.geracao}")

            plt.legend(loc="upper right")

            plt.grid(True, linestyle="--", alpha=0.4)

            plt.tight_layout()

            plt.savefig(f"{self.pasta}/populacao/geracao_{g.geracao}.png")

            plt.close()


def plotar_fitness_medio(historico, pasta):
    geracoes = []
    medias = []

    for g in historico:
        # eixo x
        geracoes.append(g.geracao)
        # eixo y
        medias.append(g.media)

    plt.figure()
    plt.plot(geracoes, medias)
    plt.title("Fitness médio por geração")
    plt.xlabel("Geração")
    plt.ylabel("Fitness médio")
    plt.savefig(pasta + "/fitness_medio.png", dpi=300, bbox_inches="tight")
    plt.close()

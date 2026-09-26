import cromossomo


class Populacao:
    def __init__(self):
        self.populacao = []

    def criar_populacao(self, Max):

        for i in range(Max):
            individuo = cromossomo.Cromossomo()
            self.populacao.append(individuo)

    def imprimir_populacao(self):
        for individuo in self.populacao:
            print(
                f"individuo = {individuo.genes}  fitness = {individuo.fitness}  rank = {individuo.rank}  prob = {individuo.probabilidade:.2%}"
            )

    def ordenar_populacao(self):
        self.populacao = sorted(
            self.populacao, key=lambda crom: crom.fitness, reverse=True
        )

    def atribuir_ranking(self):
        # garante que o melhor esta no indice 0
        self.ordenar_populacao()
        # len devolve a quantidade de itens da lista e é guardando em N
        N = len(self.populacao)

        # o loop fará N interacoes . indice vai de 0 ate  N - 1 porque a contagem comeca em 0
        # melhor individuo recebe N. O segundo melhor N - 1 e assim vai , tendeu
        for indice, individuo in enumerate(self.populacao):
            individuo.rank = N - indice

    def calcular_probabilidades(self):
        self.atribuir_ranking()
        N = len(self.populacao)

        # soma dos ranks (formula)
        soma_ranks = N * (N + 1) / 2

        for individuo in self.populacao:
            individuo.probabilidade = individuo.rank / soma_ranks

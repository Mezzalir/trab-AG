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
            print(f"indiviuo = {individuo.genes}  fitness = {individuo.fitness}")

    def ordenar_populacao(self):
        self.populacao = sorted(self.populacao, key=lambda crom: crom.fitness, reverse=True)

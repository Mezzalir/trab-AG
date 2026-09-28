import random

import cromossomo


class Populacao:
    def __init__(self):
        self.populacao = []
        self.geracao = 0
        self.taxa_mutacao = 0

    def criar_populacao(self, Max):

        for i in range(Max):
            individuo = cromossomo.Cromossomo()
            individuo.criar_genes()
            individuo.calcular_fitness()
            self.populacao.append(individuo)

    def imprimir_populacao(self):
        for individuo in self.populacao:
            print(
                f"individuo = {individuo.genes} fitness = {individuo.fitness} "
                f"rank = {individuo.rank} prob = {individuo.probabilidade:.2%}"
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

    def selecionar_pais(self):
        # a roleta gira N vezes e monta a pool dos pais

        # probabilidades precisam ser calculadas antes
        self.calcular_probabilidades()

        N = len(self.populacao)

        # pool dos pais
        pais = []

        for _ in range(N):
            # gira a roleta sorteando um numero entre 0 e 1
            r = random.random()
            # a cada giro a soma recomeca o zero
            soma = 0

            for individuo in self.populacao:
                soma = soma + individuo.probabilidade
                if soma >= r:
                    escolhido = individuo
                    break
            pais.append(escolhido)

        return pais

    def aplicar_elitismo(self):
        # populacao deve estar previamente ordenada (no main.py)
        # Individuo mais apto vai direto pra nova geracao
        # sem precisar fazer crossover e mutacao
        elite = self.populacao[0]

        return elite

    def cruzamento(self):

        filho = []
        pool = self.selecionar_pais()
        pai1 = random.choice(pool)

        while True:
            pai2 = random.choice(pool)
            if pai1 != pai2:
                break

        for i in range(5):
            mascara = random.randint(1, 2)

            if mascara == 1:
                filho.append(pai1[i])
            else:
                filho.append(pai2[i])

        return filho

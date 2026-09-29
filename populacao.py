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

        self.ordenar_populacao()
        melhor = self.populacao[0]

        # cria um objeto novo, copia os genes e calcula o fitness
        elite = cromossomo.Cromossomo()
        elite.genes = list(melhor.genes)
        elite.calcular_fitness()

        return elite

    def cruzamento(self, taxa_cruzamento):

        pais = self.selecionar_pais()
        filhos = []

        # pegar pais de dois em dois
        # se N for impar o ultimo pai fica sem par
        for i in range(0, len(pais) - 1, 2):  # faz o i pular de 2 em 2
            pai1 = pais[i]
            pai2 = pais[i + 1]

            # os filhos ocomecam como copias dos papais
            genes_filho1 = list(pai1.genes)
            genes_filho2 = list(pai2.genes)

            # sorteia se este par vai cruzar, conforme a taxa
            if random.random() < taxa_cruzamento:
                # cruzamento uniforme. Bit a  bit
                for j in range(len(pai1.genes)):
                    mascara = random.randint(1, 2)

                    if mascara == 1:
                        genes_filho1[j] = pai1.genes[j]
                        genes_filho2[j] = pai2.genes[j]
                    else:
                        genes_filho1[j] = pai2.genes[j]
                        genes_filho2[j] = pai1.genes[j]

            # transformar em objeto pois ate o momento eh so uma lista de numeros
            for genes in (genes_filho1, genes_filho2):
                filho = cromossomo.Cromossomo()
                filho.genes = genes
                filho.calcular_fitness()
                filhos.append(filho)

        return filhos

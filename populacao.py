import random

import cromossomo


class Populacao:
    def __init__(self, popmax=6):
        self.populacao = []
        self.pool_acasalamento = []
        self.popmax = popmax
        self.geracao = 0
        self.taxa_mutacao = 0.01
        self.taxa_cruzamento = 0.7

    def criar_populacao(self):

        for i in range(self.popmax):
            individuo = cromossomo.Cromossomo()
            individuo.criar_genes()
            individuo.calcular_fitness()
            self.populacao.append(individuo)

    def imprimir_populacao(self):
        for individuo in self.populacao:
            print(
                f"individuo = {individuo.genes} fitness = {individuo.fitness:.1f} "
                f"rank = {individuo.rank:.1f} prob = {individuo.probabilidade:.1%}"
            )

    def imprimir_pool(self):
        for individuo in self.pool_acasalamento:
            print(
                f"individuo = {individuo.genes} fitness = {individuo.fitness:.1f} "
                f"rank = {individuo.rank:.1f} prob = {individuo.probabilidade:.1%}"
            )

    def ordenar_populacao(self):
        self.populacao = sorted(
            self.populacao, key=lambda crom: crom.fitness, reverse=True
        )

    def atribuir_ranking(self):
        # garante que o melhor esta no indice 0
        # self.ordenar_populacao()
        N = len(self.populacao)

        for indice, individuo in enumerate(self.populacao):
            individuo.rank = N - indice

    def calcular_probabilidades(self):
        # self.atribuir_ranking()
        N = len(self.populacao)

        # soma dos ranks (formula)
        soma_ranks = N * (N + 1) / 2

        for individuo in self.populacao:
            individuo.probabilidade = individuo.rank / soma_ranks

    def selecionar_pais(self):
        # a roleta gira N vezes e monta a pool dos pais

        # probabilidades precisam ser calculadas antes
        # self.calcular_probabilidades()

        N = len(self.populacao)

        # pool dos pais
        pool = self.pool_acasalamento

        for _ in range(N):
            r = random.random()
            # a cada giro a soma recomeca o zero
            soma = 0

            for individuo in self.populacao:
                soma = soma + individuo.probabilidade
                if soma >= r:
                    escolhido = individuo
                    break
            pool.append(escolhido)

    def aplicar_elitismo(self):

        melhor = self.populacao[0]

        elite = cromossomo.Cromossomo()
        elite.genes = list(melhor.genes)
        elite.calcular_fitness()

        return elite

    def cruzamento(self):

        pais = self.pool_acasalamento
        filhos = []

        # NOTE: faz parte do teste
        nova_populacao = Populacao()

        for i in range(0, len(pais) - 1, 2):
            pai1 = pais[i]
            pai2 = pais[i + 1]

            genes_filho1 = list(pai1.genes)
            genes_filho2 = list(pai2.genes)

            print()

            print(f"Pai 1 = {genes_filho1}")
            print(f"Pai 2 = {genes_filho2}")
            print()

            if random.random() < self.taxa_cruzamento:
                for j in range(len(pai1.genes)):
                    mascara = random.randint(1, 2)

                    if mascara == 1:
                        genes_filho1[j] = pai1.genes[j]
                        genes_filho2[j] = pai2.genes[j]
                    else:
                        genes_filho1[j] = pai2.genes[j]
                        genes_filho2[j] = pai1.genes[j]


            print("filhos cruzados")
            print()
            num = 1
            for genes in (genes_filho1, genes_filho2):
                filho = cromossomo.Cromossomo()
                filho.genes = genes

                print(f"Filho {num} = {filho.genes}")

                if random.random() < self.taxa_mutacao:
                    filho.mutacao()
                    filho.calcular_fitness()

                    print(f"Filho {num} = {filho.genes} <- sofreu mutacao")
                    print()

                filho.calcular_fitness()


                nova_populacao.populacao.append(filho)

                num+=1


                # filhos.append(filho)

        print("nova populacao:")
        print(nova_populacao.imprimir_populacao())
        # return filhos

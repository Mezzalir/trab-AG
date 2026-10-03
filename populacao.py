import random

import graficos
import cromossomo
import geracao
from code_e_decode import decodificar


class Populacao:
    def __init__(self, popmax, geracoes, tx_mutacao, tx_crossover):
        self.populacao = []
        self.pool_acasalamento = []
        self.num_geracoes = geracoes
        self.pop_max = popmax
        self.geracao = 0
        self.taxa_mutacao = tx_mutacao
        self.taxa_cruzamento = tx_crossover
        self.historico = []
        self.max_ranking = 1.2

    def criar_populacao(self):

        for i in range(self.pop_max):
            individuo = cromossomo.Cromossomo()
            individuo.criar_genes()
            individuo.calcular_fitness()
            self.populacao.append(individuo)

    def imprimir_populacao(self, elite):
        print(f"\nGeracao : {self.geracao}")
        for individuo in self.populacao:
            print(
                f"individuo = {individuo.genes} fitness = {individuo.fitness:.1f} "
                f"rank = {individuo.rank:.1f} prob = {individuo.probabilidade:.1%}"
            )
        individuo = elite
        print(
            f"Elite {individuo.genes} fitness = {individuo.fitness:.1f} "
            f"rank = {individuo.rank:.1f} prob = {individuo.probabilidade:.1%}\n"
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
        N = len(self.populacao)

        for indice, individuo in enumerate(self.populacao):
            individuo.rank = N - indice

    def calcular_probabilidades(self):
        N = len(self.populacao)

        # max eh quantas copias o melhor recebe em media
        Max = self.max_ranking
        Min = 2 - Max

        for individuo in self.populacao:
            individuo.probabilidade = (Min + (Max - Min) * (individuo.rank - 1) / (N - 1)) / N

    def selecionar_pais(self):

        self.pool_acasalamento = []
        N = len(self.populacao)

        for _ in range(N):
            r = random.random()
            # a cada giro a soma recomeca o zero
            soma = 0

            for individuo in self.populacao:
                soma = soma + individuo.probabilidade
                if soma >= r:
                    # escolhido = individuo
                    self.pool_acasalamento.append(individuo)
                    break

    def aplicar_elitismo(self):
        melhor = self.populacao[0]

        elite = cromossomo.Cromossomo()
        elite.genes = list(melhor.genes)
        elite.calcular_fitness()

        return elite

    def cruzamento(self):

        pais = self.pool_acasalamento.copy()
        random.shuffle(pais)
        filhos = []

        total_filhos = len(self.populacao) - 1

        if len(pais) % 2 != 0:
            novo_pai = random.choice(pais)
            pais.append(novo_pai)

        for i in range(0, len(pais) - 1, 2):
            pai1 = pais[i]
            pai2 = pais[i + 1]

            genes_filho1 = list(pai1.genes)
            genes_filho2 = list(pai2.genes)

            if random.random() < self.taxa_cruzamento:
                for j in range(len(pai1.genes)):
                    mascara = random.randint(1, 2)

                    if mascara == 1:
                        genes_filho1[j] = pai1.genes[j]
                        genes_filho2[j] = pai2.genes[j]
                    else:
                        genes_filho1[j] = pai2.genes[j]
                        genes_filho2[j] = pai1.genes[j]

            for genes in (genes_filho1, genes_filho2):

                if len(filhos) >= total_filhos:
                    return filhos

                filho = cromossomo.Cromossomo()
                filho.genes = genes

                if random.random() < self.taxa_mutacao:
                    filho.mutacao()

                filho.calcular_fitness()

                filhos.append(filho)

        return filhos

    def gerar_geracoes(self):

        for i in range(self.num_geracoes):
            self.geracao = i

            self.ordenar_populacao()
            self.atribuir_ranking()
            self.calcular_probabilidades()
            self.registrar_geracao()

            elite = self.aplicar_elitismo()
            self.selecionar_pais()

            nova_geracao = self.cruzamento()
            nova_geracao.append(elite)

            self.populacao = nova_geracao

        # Registro final da ultima geracao apos a evolucao
        self.geracao = self.num_geracoes
        self.ordenar_populacao()
        self.atribuir_ranking()
        self.calcular_probabilidades()
        self.registrar_geracao()

        # grafico da populacao em cada geracao
        grafico = graficos.GraficoPopulacao(self.historico)
        grafico.plotar_grafico_comportamento()

    def registrar_geracao(self):
        # criando os registros!!!!!!!!
        N = len(self.populacao)
        melhor = self.populacao[0]

        soma = 0
        pontos = []
        for individuo in self.populacao:
            soma = soma + individuo.fitness
            x = decodificar(individuo.genes[:5])
            y = decodificar(individuo.genes[5:])
            pontos.append((x, y))

        self.historico.append(
            geracao.Geracao(
                self.geracao,
                soma / N,
                melhor.fitness,
                decodificar(melhor.genes[:5]),
                decodificar(melhor.genes[5:]),
                pontos,
            )
        )

    def salvar_log_em_arquivo(self, nome_arquivo):
        arquivo = open("logs/" + nome_arquivo, "w")
        arquivo.write("geracao,fitness_medio,melhor_fitness,melhor_x,melhor_y\n")

        for g in self.historico:
            arquivo.write(
                f"{g.geracao},{g.media:.2f},{g.melhor_fitness:.2f},{g.melhor_x},{g.melhor_y}\n"
            )
        arquivo.close()

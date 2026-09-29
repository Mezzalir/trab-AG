from random import randint
from code_e_decode import codificar, decodificar


class Cromossomo:
    def __init__(self):
        self.genes = []
        self.fitness = 0
        self.rank = 0
        self.probabilidade = 0

    def criar_genes(self):

        x = randint(-15, 15)
        y = randint(-15, 15)
        self.genes = codificar(x) + codificar(y)

    def calcular_fitness(self):
        x = decodificar(self.genes[:5])
        y = decodificar(self.genes[5:])
        self.fitness = 2 * x**2 - 13 * x + x * y - 7 * y / 3

    def mutacao(self):
        # a e b sao os intervalos
        # laco verifica se a e b nao sao iguais
        while True:
            a = randint(0, 5)
            b = randint(0, 5)
            if b - a >= 2:
                break

        geneX_temp = self.genes[:5]
        geneX_mutado = geneX_temp[:a] + geneX_temp[a:b][::-1] + geneX_temp[b:]

        geneY_temp = self.genes[5:]
        geneY_mutado = geneY_temp[:a] + geneY_temp[a:b][::-1] + geneY_temp[b:]
        self.genes = geneX_mutado + geneY_mutado

        self.calcular_fitness()

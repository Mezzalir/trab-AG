from criar_individuo import criar_individuo, codificar, decodificar


class Cromossomo:
    def __init__(self):
        self.genes = criar_individuo()
        self.fitness = self.calcular_fitness()
        self.rank = 0
        self.probabilidade = 0

    def calcular_fitness(self):
        x = decodificar(self.genes[:5])
        y = decodificar(self.genes[5:])
        self.fitness = 2 * x**2 - 13 * x + x * y - 7 * y / 3

        return self.fitness

    # def mutacao(self):

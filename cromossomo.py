from criar_individuo import criar_individuo, codificar, decodificar


class Cromossomo:
    def __init__(self, genes=None):

        # Cria um inviduo novo aleatório OU com genes especificios (dos pais)
        if genes is None:
            self.genes = criar_individuo()
        else:
            self.genes = list(
                genes
            )  # usa list para criar uma nova list e nao usar a mesma lista do pai

        self.fitness = self.calcular_fitness()
        self.rank = 0
        self.probabilidade = 0

    def calcular_fitness(self):
        x = decodificar(self.genes[:5])
        y = decodificar(self.genes[5:])
        self.fitness = 2 * x**2 - 13 * x + x * y - 7 * y / 3

        return self.fitness

    # def mutacao(self):

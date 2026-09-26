import random
from code_e_decode import codificar, decodificar

def criar_individuo():

        x = random.randint(-15, 15)
        y = random.randint(-15, 15)

        individuo = codificar(x) + codificar(y)

        return individuo

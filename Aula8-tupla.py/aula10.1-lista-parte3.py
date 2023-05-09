#import random
from random import randint
import os

os.system("cls")
sorteio = []

for contador in range(1, 11):
    sorteio.append(randint(1, 100)) #gerando valores aleatorios e salvando na lista

valor = randint(1, 100)
print(sorteio)
sorteio.sort(reverse=True)
os.system("pause") # irá pausar o sistema até uma tecla ser pressionado

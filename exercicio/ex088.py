#Crie um proagrama onde 4 jogadores jogue um dado e tenham resultado aleatórios. Guarde esses resultado em um dicionário. No final, coloque esse dicionáiro em ordem , sabendo que o vencedor tirou o maior número no dado 

from random import randint
from time import sleep
from operator import itemgetter

jogo = {"Jogador1": randint(1,6),
        "jogador2": randint(1,6),
        "jogador3": randint(1,6),
        "jogador4": randint(1,6)
}

ranking = dict()
print("Valores sorteados: ")
for k, v in jogo.items():
    print(f"{k} tirou {v} no dado.")
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking)

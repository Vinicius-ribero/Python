#Melhore o jogo onde o computador vai "Pensar" em um número entre0 e 10.Só que agora o jogador vai tentar adivinhar até acdertar, mostrando no final quantos palpites foram nescessários para vencer.


import random
from random import randint

print("-=" * 10)
computador = randint(0,10)
palpites = 0
jogador = int(input("Em que número eu pensei"))
print("-="*10)
while jogador != computador:
    if jogador > computador:
        print("Menos... tente outra vez.")
    else:
        print("Mais... tente outra vez.")
    palpites += 1
    jogador = int(input("Qual seu novo palpite?"))
print(f"Parabéns você acertou com {palpites} palpites")
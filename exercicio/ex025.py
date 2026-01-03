import random
from random import randint
from time import sleep
#FAZ COMPUTADOR PENSAR
computador = randint (0,5) 
print("-=-" *20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar")
print("-=-"*20)
#JOGADOR TENTA ADIVINHAR
jogador = int(input("Em que número eu pensei?"))
print("PROCESSANDO....")
sleep(3)
if jogador == computador:
    print("Parabéns!Você consegui me vencer!")
else: 
    print("Você perdeu! tente novante ")
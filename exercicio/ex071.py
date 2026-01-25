#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupia Depois disso, mostre a listagem de números indique e também indique o menor e o maior valor que estão na tupla

from random import randint
sorteio = randint(0,10), randint(0,10), randint(0,10), randint(0,10)
maior = max(sorteio)
menor = min(sorteio)

print(f"Os valores sorteado foram {sorteio}")
print(f"O maior valor sorteado foi {maior}")
print(f"O maior valor sorteado foi {menor}")


print("-="*20)
# COM O FOR

from random import randint

sorteio = (randint(1,10), randint(1,10), randint(1,10) ,randint(1,10), randint(1,10) )
print("Os valores sorteados forma: ", end=" ")

for n in sorteio:
    print(f"{n}", end="")

print(f"\nO maior valor  sorteado foi {max(sorteio)}")
print(f"O maior valor  sorteado foi {min(sorteio)}")
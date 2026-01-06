from random import randint
from time import sleep

itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)

print("""Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")

jogador = int(input("Qual é a sua jogada? "))

# Perfumaria: um efeito de carregamento
print("JOU")
sleep(0.5)
print("KEN")
sleep(0.5)
print("PÔ!!!")

print("-=" * 11)
# Aqui usamos a tupla 'itens' para converter o número no nome do objeto
print(f"Computador jogou: {itens[computador]}")
print(f"Jogador jogou: {itens[jogador]}")
print("-=" * 11)

# Lógica para definir o vencedor
if computador == 0: # Computador jogou PEDRA
    if jogador == 0:
        print("EMPATE!")
    elif jogador == 1:
        print("JOGADOR VENCE")
    elif jogador == 2:
        print("COMPUTADOR VENCE")
    else:
        print("JOGADA INVÁLIDA!")

elif computador == 1: # Computador jogou PAPEL
    if jogador == 0:
        print("COMPUTADOR VENCEU")
    elif jogador == 1:
        print("EMPATE!")
    elif jogador == 2:
        print("JOGADOR VENCEU")
    else:
        print("JOGADA INVÁLIDA!")

elif computador == 2: # Computador jogou TESOURA
    if jogador == 0:
        print("JOGADOR VENCEU")
    elif jogador == 1:
        print("COMPUTADOR VENCEU")
    elif jogador == 2:
        print("EMPATE!")
    else:
        print("JOGADA INVÁLIDA!")
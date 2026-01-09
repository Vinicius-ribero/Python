num = int(input("Digite um número: "))
tot = 0

for c in range(1, num + 1):
    if num % c == 0:
        print("\033[33m", end="") # Amarelo para divisíveis
        tot += 1
    else:
        print("\033[31m", end="") # Vermelho para não divisíveis
    
    print(f"{c} ", end="\033[m") # Imprime o número e RESETA a cor

print(f"\n\nO número {num} foi divisível {tot} vezes.")

if tot == 2:
    print("E por isso ele é \033[32mPRIMO!\033[m") # Verde para Primo
else:
    print("E por isso ele \033[31mNÃO É PRIMO!\033[m") # Vermelho para Não Primo
#CRIE UM PROGAMA ONDE O USUARIO possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e imapres. No final ,mostre os valores pares e impares m ordem crescente

valores = [[], []]

for c in range(1,8):
    n = int(input(f"Digite o {c}o. valor:"))
    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)

valores[0].sort()
valores[1].sort()

print(f"Os valores pares digitado foram: {valores[0]}")
print(f"Os valores ímpares digitados foram: {valores[1]}")
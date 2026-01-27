#Faça um programa que leia 5 valores númericos e gguardeos em uma lista.No final mostre qual foi o maior e menor valor
#digitado e as suas respectivas posições na lista.
num = list()
for c in range(0,5):
    num.append(int(input(f"Digite um valor para a Posição {c}: ")))

print("=-" *20)
print(f"Você digitou os valores {num}")

maior = max(num)
menor = min(num)

print(f"O maior valor digitado foi 5 nas posições ", end=" ")

for i, v in enumerate(num):
    if v == maior:
        print(f"{i}", end=" ")
print()

print(f"O menor valor digitado foi {menor} nas posições ", end=" ")
for i, v in enumerate(num): 
    if v == menor:
        print(f"{i}......", end=" ")
print()


#OUTRA VERSÃO

print("-="*50)
listanum = []
maior = 0
menor = 0

for c in range(0,5):
    listanum.append(int(input(f"Digite um valor para a Posição {c}")))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c]  < menor:
            menor = listanum[c]
print("=-" *50)
print(f"O você digitou os valores {listanum}")
print(f"O maior valor digitado foi {maior} nas posições", end="")

for i, v in enumerate(listanum):
    if v == maior:
        print(f"{i}...", end="")
print(f"O menor valor digitado foi {menor} nas posições", end="")
for i, v in enumerate(listanum):
    if v == menor:
        print(f"{i}...", end="")

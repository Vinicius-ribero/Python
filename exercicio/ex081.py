#Faça um progama que leia o nome e peso de várias pessoas, guradando tudo em uma lista. No final , mostre:
#A) Quantas pessoas foram cadastrada.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves


pessoas = list()
dado = list()
maior = menor = num =  0

while True:
    dado.append(str(input("Nome: ")))
    peso = float(input("Peso: "))
    dado.append(peso)

    #Maior ou menor peso:
    if len(pessoas) == 0:
            maior = menor = peso
    else:
        if peso > maior:
            maior = peso
            
        if peso < menor:
            menor = peso
        
    pessoas.append(dado[:])
    dado.clear()
           
    resp = str(input("Quer continuar? [S/N] ")).strip().upper()
    if resp == num:
        print(resp)
    else:
       if  resp == "N":
        break

print("-=" * 40)
print(f"Ao todo, você cadastrou {len(pessoas)} pessoas.")
print(f"O maior peso foi de {maior}.kg. Peso de: ", end= " ")
for p in pessoas:
    if p[1] == maior:
        print(f"{p[0]}", end="")
print(f"\nO menor peso foi de {menor}kg. Peso de: ", end="")
for p in pessoas:
    if p[1] == menor:
        print(f"[{p[0]}] ", end="")



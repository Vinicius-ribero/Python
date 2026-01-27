#Crie um progama que vai ler vários números e colcoar em uma lista. Depois disso , mostre:
#A)Quantos números foram digitados.

#B)A lista de vaçlores ordenada de forma descrescente.

#C)Se o valor 5 foi digitado e está ou não na lista.

num = list()

while True:
    n = int(input("Digite um valor: "))
    num.append(n)

    res = str(input("Quer continuar? [S/N]")).strip().upper()
    if res == "N":
        break
print("-" * 30)

print(F"Você digitou {len(num)} elementos")

num.sort(reverse=True)
print(f"Os valores em ordem descrente são {num}")

if 5 in num:
    print("O valor 5 faz parte da lista! e está na ")
else:
    print("O valor 5 não faz parte da lista")
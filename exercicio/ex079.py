#Crie um programa que vai ler vários números e colocar em um a lista. Depois disso, crie duas lista extras que vão conter valores pares e os valores impares digitados, respectivamente. Ao final mostre o conteúdo das três lista geradas.

lista = []
listaPar = []
listaImpar = []

while True:
    n = int(input("Digite um número: "))
    lista.append(n)

    res = str(input("Quer continuar [S/N]: ")).strip().upper()
    if res == "N":
        break

# O "for" deve começar aqui, na mesma linha (coluna) do "while"
for valor in lista:
    if valor % 2 == 0:
        listaPar.append(valor)
    else:
        listaImpar.append(valor)

print("-="*30)
print(f"A lista completa é {lista}")
print(f"A lista de pares é {listaPar}")
print(f"A lista de ímpares é {listaImpar}")
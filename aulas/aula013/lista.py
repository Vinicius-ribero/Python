num = [2, 5, 9, 1]
num [2] = 3
num.append(7) #Adiciona o valor(7)
num.sort(reverse = True)
num.insert(2,2)    #Na posição 2 ele vai adicionar um valor 0
# num.pop()   Remove o ultimo número
if 5 in num:
    num.remove(5)
else:print("Não achei o número 4")

print(num)
print(f"Essa lista tem {len(num)} elementos")


valores =   []  #Ou list()
valores.append(5)
valores.append(9)
valores.append(4)
valores = list()
for cont in range(0,5):
    valores.append(int(input("Digite o valor: ")))

for v in valores:
    print(f"{v}...", end="")

for c, v in enumerate(valores):
    print(f"Na posição {c} encontrei o valor {v}")


a = [2,3,4,7]
b = a #[:] este simobolo criaria uma copia do valores e não mudaria a lista 
b[2] = 8 

print(f"Lista A: {a}")
print(f"Lista B: {b}")


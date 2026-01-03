one = int(input("Primeiro Valor: "))
second = int(input("Segundo Valor: "))
tre = int(input("Terciero Valor: "))

menor = one
if second < one and second < tre:
    menor = second
if tre < one and tre < second:
    menor = tre

#MAIOR

maior = one
if second > one and second > tre:
    maior = second
if tre > one and tre > second:
    maior = tre


print(f"O menor valor foi digitado foi {menor}")
print(f"O maior valor digitado foi {maior}")


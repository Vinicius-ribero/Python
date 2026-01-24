#Faça um programa que leia um número qualquer e mostre seu fatorial

number = int(input("Digite um número: ")
)
c = number
f = 1
while c > 0:
    print(f"{c}", end= "")
    print("x" if c >1  else "=" , end= "")

    f *= c
    c -= 1
print(f"f")


#FOR 

n = int(input("Digite um número: "))
f = 1

print(f"Calculando {n}! = ", end="")

for c in range(n, 0, -1):
    print(f"{c}", end="")
    
    # Se o número atual for maior que 1, coloca o 'x', senão coloca o '='
    if c > 1:
        print(" x ", end="")
    else:
        print(" = ", end="")
    
    f *= c

print(f"{c}")
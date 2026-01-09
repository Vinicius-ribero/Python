#faça um programa que calcule a soma entre todos os númeors impares que são mútiplos de três e que se ecnocontarm no intervalo de 1 até 500
soma = 0
count = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c 
        count = count + 1
        
print(f"A soma de todos os {count} é igual a {soma}.")
    
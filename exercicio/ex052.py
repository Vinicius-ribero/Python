#Faça um progama que leia o peso de cinco pessoas .No final mostre qual foi a maior e menor peso lido.

maior = 0
menor = 0


for p in range(1, 6):
    peso = float(input(f"Digite o peso da {p}ª pessoas (kg) : "))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso 

        if peso < menor:
            menor = peso

            
print('-' * 20)
print(f'O maior peso lido foi de {maior}kg')
print(f'O menor peso lido foi de {menor}kg')
        
    
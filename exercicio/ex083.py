#Crie um programa que crie uma matrizde dimensão de 3x3 e preencha com valores lidos pelo teclado. No final mostre a matriz na tela com a formatação correta.


lista = [[], [], []]


for c in range(0, 3):
    n = int(input(f"Digite um valor para [0, {c}]: "))
    lista[0].append(n) 


for c in range(0, 3):
    n = int(input(f"Digite um valor para [1, {c}]: "))
    lista[1].append(n) 


for c in range(0, 3):
    n = int(input(f"Digite um valor para [2, {c}]: ")) 
    lista[2].append(n) 

print("-=" * 20)

print(lista[0])
print(lista[1])
print(lista[2])

print("-="*50)

#Versão inteligente

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Alimentando a matriz
for l in range(0, 3):    # Laço para as LINHAS
    for c in range(0, 3): # Laço para as COLUNAS
        matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))

print("-=" * 30)

# Mostrando a matriz com formatação
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end='') # O :^5 centraliza o número
    print() # Pula linha ao final de cada linha da matriz
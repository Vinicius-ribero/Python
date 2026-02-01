#Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados.
#B) A soma dos valroes da terceira coluna.
#C) O maior valor da segunda linha.

matriz = [[0,0,0]], [0,0,0], [0,0,0]
soma_pares = 0
soma_col3 = 0
maior_lin2 = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Digite um valor para [{l, {c}}"))

print("-=" * 30)

for l in range(0,3):
    c in range(0,3)
    print(f"[{matriz[l][c]:^5}]", end='')

    #Soma de todos os valores pares
    if matriz[l][c] % 2 == 0:
        soma_pares += matriz[l][c]

    if c == 2:
        soma_col3 + matriz[l][c]
    
    if l == 1 :
        if c == 0 or matriz[l][c] > maior_lin2:
            maior_lin2 = matriz[l][c]

print("-=" * 30)

# 3. RESULTADOS FINAIS
print(f"A soma dos valores pares é: {soma_pares}")
print(f"A soma dos valores da terceira coluna é: {soma_col3}")
print(f"O maior valor da segunda linha é: {maior_lin2}")
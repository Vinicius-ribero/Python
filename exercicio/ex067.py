#CRIE UM PROGAMA QUE LEIA O NOME E O PREÇO DE VÁRIOS PRODUTOS. O PROGAMA DEVERÁ PERGUNTAR SE O USUÁRIO VAI CONTINUAR. NO FINAL, MOSTRE:
#A) QUAL É O TOTAL GASTO NA COMPRA.
#B) QUANTOS PRODUTOS CUSTAM MAIS DE R$ 1000
#C) QUAL É O NOME DO PRODUTO MAIS BARATO

print("-"*30)
print("   LOJA SUPER BARATÃO")
print("-"*30)

cont = total = total_mil = menor_preço = mais_barato = 0


while True:
    produto = str(input("Digite o nome do Produto: ")).strip()
    preço = int(input("Preço: "))
    total += preço
    cont += 1

    # Lógica do mais barato (Simplificada
    if cont ==  1 or preço < menor_preço:
        menor_preço = preço
        mais_barato = produto

     # Contagem de produtos acima de 1000
    if preço > 1000:
        total_mil += 1

 
    
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N]: ")).upper().strip()

    print("-" * 30)
    if resp == "N":
        break


print("---------- FIM DO PROGAMA ---------- ")
print(f"O total da compra foi {total}")
print(f"Temos {total_mil} produtos custando mais de R$ 1000.00 ")
print(f"O produto mais barato foi {mais_barato} que custa {menor_preço}")
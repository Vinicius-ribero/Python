#CREI UM PROGAMA QUE SIMULE O FUNCIONAMNETO DE UM CAIZA ELETRÔNIC. NO INICIO, PERGUNTE AO USUÁRIO QUAL SERÁ O VALOR A SER SACADO (NÚMERO INTIERO) E O PROGAMA VAI INFORMAR QUNATAS CÉDULAS DE VALOR SERÃO ENTREGUES.
#OBS: CONSIDERE QUE O CAIXA POSSUI CÉDULA DE R$50, R20$, R%$10 E R$1

print("="*30)
print(f"{'BANCO CEV':^30}")
print("="*30)

valor = int(input("Qual valor você quer sacar? R$ "))
total = valor
céd = 50
totalCéd = 0

while True:
    if total >= céd:
        total -= céd
        totalCéd += 1
    else:
        if totalCéd > 0:
            print(f"Total de {totalCéd} cédulas de R${céd}")
        
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        
        totalCéd = 0
        
        if total == 0:
            break

print("="*30)
print("Saque finalizado. Volte sempre!")

for c in range(0, 10, 3):
    print(c)
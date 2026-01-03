ano = int(input("Digite um ano: "))

if ano % 4 == 0:
    print(f"Você está em {ano} um ano considerado bissexto")
else:
    print(f"Voçê não está em um ano bissexto")


#AVANÇADO

ano = int(input("Digite um ano: "))

if ano % 4 == 0:
    if ano % 100 == 0: # É um ano centenário? (Ex: 1900, 2000)
        if ano % 400 == 0: # Centenários só são bissextos se dividirem por 400
            print("É Bissexto")
        else:
            print("Não é Bissexto")
    else:
        print("É Bissexto")
else:
    print("Não é Bissexto")


#AVANÇADO

from datetime import date
ano = int(input("Que ano quer analisr? Coloque 0 para analisar o ano atual: "))
if ano == 0:
    ano = date.today(). year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} é BISSEXTO")
else:
    print(f"O ano {ano} não é BISSEXTO")
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
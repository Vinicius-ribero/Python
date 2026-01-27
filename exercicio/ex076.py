#Crie um Programa onde possa digitar vários valores númericos e cadastre-os em uma lista.Caso o número já exista



num = list()
while True:
    n = int(input("Digite um valor: "))
    if n not in num:
        num.append(n)
        print("Valor adicionado com sucesso...")
    else:
       print("Valor duplicado! Não posso adicionar um valor que não seja um número!")
    resp = str(input("Quer continuar [S/N]").strip().upper())
    if resp == "N":
        break
print("-="*40)
print(f"Você digitou os valores {sorted(num)}")

#CRIE UM PROGAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO. NO FINAL DA EXECUÇÃO, MOSTRE A MÉDIA ENTRE TODOS OS VALORES E QUAL FOI O MAIOR E O MENOR VALORES LIDOS. O PROGAMA DEVE PERGUNTAR AO USUÁRIO  SE ELE QUER OU NÃO CONTINUAR A DIGITAR VALORES  

resp = "S"
soma = média = quant = 0

while resp in "Ss":
    num = int(input("Digite um número: "))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input("Quer continuar? [S/N]").strip())
média = soma /quant
print(f"Você digitou {quant} números e a média foi {soma}")
print(f"O mairo valor foi {maior} e o menor foi{menor}")


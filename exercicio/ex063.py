#CRIE UM PROGAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO. O PROGRAMA SÓ VAI PARAR QUANDO O USUÁRIO DIGITAR O VALOR 999
#QUE É A CONDIÇÃO DE PARADA. NO FINAL MOSTRE QUANTOS NÚMEROS FORAM DIGITADOS E QUAL FOI A SOMA ENTRE ELES

n = s = cont = 0
while True:
    n = int(input("Digite um valor ou (999 para parar) "))
    if n == 999:
        break
    s += n
    cont +=1 
print(f"A soma dos  {cont} valores é igual a {s}!!")


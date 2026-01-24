#CRIE UM PROGAMA QUE LEIA VÁRIOS NÚMROS INTEIROS PELO TECLADO . O PROGAMA SÓ VAI PARAR QUANDO O USUÁRIO DIGITAR O VALOR 999, QUE É CONDIÃO DE PARADA. NO FINAL MOSTRE QUANTOS NÚMEROIS FORAM DIGITADOS E QUAL FOI A SOMA ENTRE ELES (DESCONSIDERANDO O FLAG)

number = 0
cont = 0 
soma = 0

while True: # Usar True aqui é mais comum com o break
    n = int(input("Digite um número (999 para parar): "))
    
    if n == 999: # 1º Verifica se é a parada
        break    # Se for 999, sai do loop IMEDIATAMENTE sem somar
        
    # Se o programa chegou aqui, é porque o número NÃO é 999
    soma += n    # 2º Soma o número válido
    cont += 1    # 3º Conta o número válido

print(f"Você digitou {cont} números e a soma foi {soma}.")
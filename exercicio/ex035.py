#ESCREVAUM PROGAMA QUE LEIA DOIS NÚMEROS INTEIROS E COMPARE-OS MOSTRANDO NA TELA UM A MENSAGEM: 
# O PRIMEIRO VALOR É MAIOR
# O SEGUNDO VALOR É MAIOR:
#NÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS

number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))

if number1 > number2:
    print(f"O primeiro número \033[33m{number1}\033[m é maior que \033[34m{number2}\033[m")
elif number2 > number1:
    print(f"O segundo valor \033[32m{number1}\033[m é maior quo primeiro \033[35m{number2}\033[m")
else:
    print("Não existe vaor maior, os dois são iguais")

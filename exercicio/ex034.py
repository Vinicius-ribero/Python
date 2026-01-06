#ESCREVA UM PROGAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E PEÇA PARA O USUÁRIO ESCOLHER QUAL SERÁ A BASA DE SUA CONVERSÃO:
# -1 PARA BINÁRIO
# -2 PARA OCTAL
# -3 PARA HEXADECIMAL

num = int(input("Digite um número inteiro: "))
print("Escolha uma das bases de conversão: "
"[1] converter para BINÁRIO"
"[2] converter ara OCTAL"
"[3] converter para HEXADECIMAL")
opção = int(input("Sua opção:"))
if opção == 1:
    print(f"{num}convertido para BINÁRIO é igula a {bin(num)}")
elif opção == 2:
    print(f"{num}convertido para OCTAL é igula a {oct(num)}")
elif opção == 3:
    print(f"{num} convertido para HEXADECIMAL é igual a {hex(num)}")
else:
    print("OPÇÃO INVÁLIDA!TENTE NOVAMENTE")

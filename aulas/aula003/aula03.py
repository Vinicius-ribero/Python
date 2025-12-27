#OPERADORES 

# + == ADIÇÃO  5+2 == 7
# - ==  SUBTRAÇÃO 5-2 == 3
# * == MULTIPLICAÇÃO 5 * 2 == 10
# / == DIVISÃO 5 /2 == 2.5
# ** == POTÊNCIA 5** 2 == 25
# \/ == DIVISÃO INTEIRA 5 // 2 
# /%  == RESTO DA DIVISÃO  5 % 2  


#ORDEM DE PRECEÊNCIA  = (),**, * / // % ,+ - 

n1 = int(input("Um valor:"))
n2 = int(input("Outro valor: "))
soma = n1 + n2
multiplicação = n1 * n2
Divisão = n1 / n2 
DivisãoInteira = n1 // n2
Exponenciação = n1 ** n2

print(f"O resultado da soma dos valores {n1 , n2} é de {soma} a  mulitplicação desses valores  é {multiplicação}, sua divisão é {Divisão}, e divisão Inteira é igual a {DivisãoInteira}, e sua exponeciação é igual a {Exponenciação}.")
#A confederação Nacional de Natação prescisa de um progama que leia o ano de nascimneto de um atltea e mostre sua categori, de acordo com sua idade:

#até 9anovs:mirim
# até 14 anos: Infantil
#Até 19 anos: Junior
# Até 20 anos :senior
#Acima Master 

from datetime import date
atual = date.today().year #IDADE ATUAL
ano = int(input("Ano de Nascimento: "))
idade  = atual - ano
if idade <= 9:
    print("MIRIM")
elif idade <=14:
    print("INFANTIL")
elif idade <= 19:
    print("JUNIOR")
elif idade <=20:
    print("SÊNIOR")
else:
    print("MASTER")


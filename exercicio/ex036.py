#Faça um progama que leia o ano de nascimneto de um jovem e informe, de acordo com sua idade:
#se ele ainda vai se alistar ao serviço militar:
#se é a hora de se alistar
#se já passou do tempo do seu alistamento:

#Seu progama também deverá mostrar o tempo que falta ou que passou do prazo 

from datetime import date 

atual = date.today().year
nasc = int(input("Em que ano você nasceu? "))
idade = atual - nasc

print(f"Quem nasceu em {nasc} tem {idade} anos em {atual}")

if idade == 18:
    print("Você tem que se alistar imediatamente")
elif idade < 18:
    saldo = idade - 18
    ano_alistamento = atual + saldo
    print(f"Ainda faltam {saldo} anos para o alistamento")
    print(f"Seu alistamento será em {ano_alistamento}.")
else:
    saldo = idade - 18
    ano_alistamento = atual - saldo
    print(f"Você deveria ter se alistado há {saldo} anos.")
    print(f"Seu alistamento foi em {ano_alistamento}.")

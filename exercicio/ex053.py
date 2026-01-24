#DESENVOLVA UM PROGAMA QUE LEIA O NOME, IDADE, E SEXO DE 4 PESSOAS . NOM FINAL DO PROGAMA MOSTRE 
# A média de Idade do GRupo.
#QUAL É O NOME DO HOMEM MAIS VELHO.
#QUAL MULHERES TEM MENOS DE 20ANOS.


somaidade = 0
media = 0
maioridadehomem = 0 
nomevelho = ""
totmulher20 = 0 

for p in  range(1,5):
    print(f"-----{p}ª")
    nome = str(input(f"Nome"))
    idade = int(input("idade : "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    somaidade += idade
    if p == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Mm" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo  in "Ff" and idade < 20:
        totmulher20 +=  1

mediaidade = somaidade / 4
print(f"A média de idade do grupo é de {mediaidade}anos")
print(f"O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}")
print(f"Ao todo são {totmulher20} mulheres com menos de 20 anos.")
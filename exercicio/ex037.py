#Crie um programa que leia duas notas de um aluno (a) e calcula sua média, mostrando uma mensagem no final , de acordo com sua média atingida:

#Média abaixo de 5.0 REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#MÉDIA 7.0 OU SUPERIOR: APROVADO


nota1 = float(input("Digite sua primeira nota? "))
nota2 = float(input("Digite sua segunda nota? "))
média = (nota1 + nota2) / 2

if média < 5.0:
    print("Status: REPROVADO")
elif 5.0 <= média < 7.0: # Se não for menor que 5, mas for menor que 7
    print("Status: RECUPERAÇÃO")
else: # Se não caiu em nenhuma das anteriores, só pode ser 7.0 ou mais
    print("Status: APROVADO")
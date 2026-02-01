#Faça um programa que leia nome e méda de um aluno, huradando também a situação em um dicionario.No final, mostre o conteúdo da estrutura da tela.

notas = dict()
dicionario_nome = dict()
dicionario_media = dict()
dicionario_situacao  = dict()

notas["nome"] = str(input("Nome: "))
notas["média"] = float(input(f"média {notas["nome"]}: "))
print(f"O nome é igual a {notas['nome']}")
print(f"A média é igual a {notas["média"]}")
if notas["média"] > 6.0:
        print(f"A situação é igual aprovado!")
else:
        print("A situação é igual a Reprovado")


#Versão mais complexa

# Guardando as entradas direto nas chaves do dicionário
notas = dict()
notas["nome"] = str(input("Nome: "))
notas["média"] = float(input(f"Média : "))

# Lógica para definir e guardar a situação
if notas["média"] >= 7.0:
        notas["situação"] = "Aprovado"
else:
        notas["situação"] = "Reprovado"

#Mostrando o dicionário completo
print("-=" *30)
print(notas)

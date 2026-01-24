#CRIE UM PROGAMA QUE LEIA A IDADE E O SEXO DE VÁRIAS PESSOAS. A CADA PESSOS CADASTRADA, O PROGAMA DEVERÁ
#PERGUNTAR SE O USUÁRIO QUER OU NAO QUER CONTINUAR. NO FINAL MOSTRE:
#QUANTAS PESSOAS TEM MAIS DE 18 ANOS.
#QUANTOS HOMENS FORAM CADASTRADOS


# print("-"*20)
# print("CADASTRE UMA PESSOA")
# print("-"*20)

# resp = "Ss"
# maioridade  = homens = mulheres_menor_idade = 0


# while resp in "Ss" :
#     idade = int(input("Idade: "))
#     sexo = str(input("Sexo: [M/F] ").upper().strip())
#     resp = str(input("Quer continuar? [S/N]".upper().strip()))
#     print("-"*20)
#     if sexo == "M":
#         maioridade+= 1
#     if idade > 18:
#         maioridade +=1
#     if sexo == "F" and idade < 20:
#         mulheres_menor_idade +=1
#     if resp == 'N':
#         break

# print("====== FIM DO PROGRAMA =======")
# print(f"Total de pessoas com mais de 18 anos: {maioridade}")
# print(f"Ao todo temos {homens} homens cadastrados")
# print(f"E temos {mulheres_menor_idade} mulheres com menos de 20 anos")

#CORRIGIDO 

print("-" * 20)
print("CADASTRE UMA PESSOA")
print("-" * 20)

maioridade = homens = mulheres_menor_idade = 0

while True:
    idade = int(input("Idade: "))
    
    # Validação do Sexo (para não aceitar qualquer letra)
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo: [M/F] ")).upper().strip()[0]
    
    # Lógica de contagem
    if idade > 18:
        maioridade += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20:
        mulheres_menor_idade += 1
    
    # Pergunta se quer continuar
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    
    print("-" * 20)
    if resp == "N":
        break

print("====== FIM DO PROGRAMA =======")
print(f"Total de pessoas com mais de 18 anos: {maioridade}")
print(f"Ao todo temos {homens} homens cadastrados")
print(f"E temos {mulheres_menor_idade} mulheres com menos de 20 anos")
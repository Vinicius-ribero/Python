

dados = dict()
dados = {"Nome":"Pedro", "idade": "25"}
del dados["idade"]
print("=-"*40)

print(dados["Nome"])
print(dados["idade"])

print("=-"*40)


filme = {"titulo": "Star wars",
          "Ano" : "1977",
          "diretor" : "George Lucas"}

print(filme.values())   #Seleciona os valores do dicionario
print(filme.keys())     #Seleciona a categoria do dicionario print(filme.items())    #Seleciona tudo

print("-="*40)

for k, v in filme.items():
    print(f"O {k} é {v}")

print("-="*40)
pessoas = {"Nome": "Gustavo", "sexo": "M", "idade": 22}
print(f"O {pessoas['Nome']} tem {pessoas['idade']} anos")
print(pessoas.keys())       #Seleciona os valores do dicionario
print(pessoas.values())     #Seleciona a categoria do dicionario
print(pessoas.items())      #Seleciona tudo

for k in pessoas.keys():
    print(k)    

print("-="*40)

for k in pessoas.values():
    print(k)

print("-="*40)

for k, v in pessoas.items():
    print(f"{k} = {v}")


print("-="*40)
pessoas = {"Nome": "Gustavo", "sexo": "M", "idade": 22}
del pessoas["sexo"]
for k, v in pessoas.items():
    print(f"{k} = {v}")


#Adicionando um elemento 

print("-="*40)
pessoas = {"Nome": "Gustavo", "sexo": "M", "idade": 22}
pessoas["peso"] = 98.5
for k, v in pessoas.items():
    print(f"{k} = {v}")


#Dicionario dentro de uma Lista
print("-="*40)
brasil = []
estado1 = {"uf": "Rio de janeiro", "sigla": "RJ" }
estado2 = {"uf": "São Paulo", "sigla": "SP"}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0])     #Mostra RJ
print(brasil[1])     #Mostra SP

print(brasil[0] ["uf"]) 
print(brasil[1] ["sigla"])  

print("-="*40)

estado = dict()
brasil = list()
for c in range(0,3):
    estado["uf"] = str(input("Unidade Federativa: "))
    estado["sigla"] = str(input("Sigla do Estado: "))
    brasil.append(estado.copy())
for e in brasil:
    # print(e)
    # for k, v in e.items():
    #     print(f"O campo {k} tem valor {v}")
    for v in e.values():
        print(v, end="")
    print()







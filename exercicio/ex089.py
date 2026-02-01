#Crie um programa que leia o nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade com quantos ano a pessoas vai ser aposentar

from datetime import date

ano_atual = date.today().year

dados = dict()

dados["Nome"] = str(input("Nome: "))
nascimento  = int(input("Ano de Nascimento: "))
dados["Idade"] =  ano_atual - nascimento
dados["CTPS"] = int(input("Carteira de Trabalho (0 ou não tem): "))

if dados["CTPS"] != 0:
    dados["Contratação"] = int(input("Ano de contratação: "))
    dados["salário"] = int(input("Salário: R$ "))
    dados["Aposentadoria"] = dados["Idade"] + ((dados["Contratação"] + 35) -ano_atual)
else:
    for k, v in dados.items():
        print(f"- {k} tem o valor {v}")


print("-"* 60)
print(dados.items())
for k , v in dados.items():
    print(f"- {k} tem o valor {v}")



#Por que usamos Dicionários aqui?


# Imagine que você está organizando uma ficha cadastral. Em uma Lista, você teria apenas os valores: ['João', 25, 1234]. Você teria que lembrar que o índice 0 é o nome e o 1 é a idade.

# No Dicionário, cada informação tem uma etiqueta (Label):

# Chave: "Nome" -> Valor: "João" > k

# Chave: "Idade" -> Valor: 25 > v

# Isso torna o código muito mais legível e fácil de manter.
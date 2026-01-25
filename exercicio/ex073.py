#Crie um programa que tenha uma tupla única com nomes de produtos e seus repectivos preços na sequência.No final mostre uma listagem de preços organizando os dados de forma tabular.

# print("-"*50)
# print("               LISTAGEM DE PREÇOS")
# print("-"*50)


# produtos = ["Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferido", 4.20, "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90]

# for cont in range(0,len(produtos)):
#     print(f"{produtos[0]}...............R$ {produtos[1]}")
#     print(f"{produtos[2]}...............R$ {produtos[3]}")
#     print(f"{produtos[4]}...............R$ {produtos[5]}")
#     print(f"{produtos[6]}...............R$ {produtos[7]}")
#     print(f"{produtos[8]}...............R$ {produtos[9]}")
#     print(f"{produtos[10]}...............R$ {produtos[11]}")
#     print(f"{produtos[12]}...............R$ {produtos[13]}")
#     print(f"{produtos[14]}...............R$ {produtos[15]}")
#     print(f"{produtos[16]}...............R${ produtos[17]}")
#     break



#PROFISSIONAL

print("-" * 50)
print(f'{"LISTAGEM DE PREÇOS":^50}') # Centraliza o texto em 50 espaços
print("-" * 50)

# Usando tupla () conforme o enunciado
produtos = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00,
            "Transferidor", 4.20, "Compasso", 9.99, "Mochila", 120.32, 
            "Canetas", 22.30, "Livro", 34.90)

# O loop pula de 2 em 2 (item e preço)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        # Alinha o nome à esquerda (<) em 30 espaços com pontos
        print(f"{produtos[pos]:.<40}", end="")
    else:
        # Alinha o preço à direita (>) em 7 espaços com 2 casas decimais
        print(f"R${produtos[pos]:>7.2f}")

print("-" * 50)

    
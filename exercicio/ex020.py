nome = input("Digite seu nome: ")
palavras = nome.split()
primeiro_nome = palavras[0]
quantidade_letras = len(primeiro_nome)
print(f"Prazer em te conhecer {nome.upper()}")
print(f"Prazer em te conhecer {nome.lower()}")
print(f"Seu nome tem {len(nome.replace("",""))} letras")
print(f"Seu primeiro nome é {primeiro_nome} e ele tem {quantidade_letras} letras")
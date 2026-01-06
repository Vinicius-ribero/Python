nome = str(input("Qual é seu nome? "))
if nome == "Vinícius":
    print("Que nome bonito!")
elif nome == "Pedro" or nome == "Maria" or nome == "Paulo":
    print(f"Seu nome é muito famoso {nome}")
elif nome in "Ana Cláudia Jéssica Juliana":
    print("Belo nome feminino")
else: 
    print("Seu nome é muito comum!")
print(f"Tenha um bom dia!{nome}")
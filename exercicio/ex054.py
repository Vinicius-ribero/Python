# Adicione os parênteses no strip() para que ele funcione
sexo = str(input("Digite seu sexo [M] ou [F]: ")).upper().strip()

while sexo != "M" and sexo != "F":
    print("Valor inválido!")
    # Aqui também precisa dos parênteses no strip()
    sexo = str(input("Tente novamente. Digite seu sexo [M] ou [F]: ")).upper().strip()

print(f"Sexo {sexo} registrado com sucesso!")

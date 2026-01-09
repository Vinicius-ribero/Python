#MELHORE O DESAFIO 061, PERGUNTANDO PARA O USUÁRIO SE ELE QUER MOSTRAR MAIS ALGUNS TERMSO. O PROGAMA ENCERRA QUANDO ELE DISSER QUE QUER MOSTRAR o TERMO 

primeiro = int(input("Primeiro termo: "))
razão = int(input("Razão da PA: "))

termo = primeiro
cont = 1
total = 0 # Acumula o total de termos mostrados
mais = 10 # Começamos querendo mostrar 10 termos

while mais != 0:
    total = total + mais
    while cont <= total:
        print(f"{termo} → ", end="")
        termo += razão
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? (Digite 0 para sair): "))

print(f"Progressão finalizada com {total} termos mostrados.")
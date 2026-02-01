#Crie um proagam que gerncie o aproveitamento de um jogador de futebol.O progam vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final tudo isso será guardado em dicionáio, incluindo o total de gols feitos durante o campeonato 

futebol = dict()
total = 0 
gols = []

futebol["Nome"] = str(input("Nome do jogador: "))
total_partidas = int(input(f"Quantas partida {futebol["Nome"]} jogou? "))

for c in range(total_partidas):
    gols.append(int(input(f"Quantos gols na partida {c}: ")))

    futebol["gols"] = gols[:]
    futebol["total"]= sum(gols)
    
print("-=" *30)
print(f"{futebol}")
for k, v in futebol.items():
    print(f"O campo {k} tem valor {v} ")

print("-=" *30)

print(f"O jogador {futebol['Nome']} jogou {total_partidas} partidas.")

for c in range(total_partidas):
    print(f"     => Na partida {c}, fez {futebol["gols"][c]} gols")



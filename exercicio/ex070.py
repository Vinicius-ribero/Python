#Crie um tupla preenchida com os 20 primeiros colocados da tabela do campeonato Brasileiro do futeboll. Na ordem de colocação Depois mostre:
#A) Apenas o 5 primeiros colocados 
#B) Os últimos 4 colocados da tabela.
#C) Uma lista com os times em ordem alfabetica
#D) Em que poisção na tabela está o time da chapcoense  ]


print("-="*30)

time = ["Corinthians", "Palmeiras", "Santos", "Grêmio", "Cruzeiro",
        "Flamengo", "Vasco", "Chapecoense", "Atlético", "Botafogo",
        "Atlético-PR", "Bahia", "São Paulo", "Fluminense", "Sport Recife", "EC Vitória", "Coritiba", "Avaí", "Ponte Preta", "Atlético-GO"]

print(f"Lista de times do Brasileirão : {time}")
print("-="*30)
print(f"Os cinco primeiros são {time[0:5]}")
print("-="*30)
print(f"Os 4 ultimos são {time[16:]}")
print("-="*30)
print(f"Times em ordem Alfabética {(sorted(time))}")
print(f"O Chapecoense está na  {time.index("Chapecoense")+1}° posição ")

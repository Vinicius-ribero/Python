distancia = int(input("Qual a distância da sua viagem? "))

if distancia <= 200 :
    preço = distancia * 0.50
    print(f"Tarifa padrão aplicada (R$ 0,50/km).")
else: 
    preço = distancia *0.45
    print(f"A tarifa promocional para longa distância  aplicada (R$ 0,45 km)")
print(f"Para uma viagem de {distancia}Km, o preço da passagem será R${preço:.2f}")
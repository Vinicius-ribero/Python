carro = input("Qual o nome do modelo do carro?")
dias = int(input("Informe a quantidade de dias que o veículo foi alugado"))
km  = float(input("Informe quantidade de km do veículo?"))

pago_dias = dias * 60
pago_km = km * 0.15
total = pago_dias + pago_km

print(f"O total a pagar do {carro} é R${total:.2f}")

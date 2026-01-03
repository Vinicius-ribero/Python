# Transformamos o input em número inteiro (int)
velocidade = int(input("Qual a velocidade do seu carro? "))
limite = 80
valor_por_km = 7

if velocidade > limite:
    # Subtraímos para achar o excesso
    km_acima = velocidade - limite
    multa = km_acima * valor_por_km
    print(f"Você foi MULTADO! Você passou {km_acima}km/h acima do limite.")
    print(f"O valor da multa é de R${multa:.2f}")
else:
    print("Continue sua jornada. Você está dentro do limite!")
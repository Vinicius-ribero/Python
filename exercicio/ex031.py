salário = float(input("Qual é seu salário? "))

if salário > 1250:
    aumento = salário * 0.10
else:
    aumento = salário * 0.15

novo_salario = salário + aumento

print(f"Seu aumento foi de R${aumento:.2f}")
print(f"Seu novo salário é de R${novo_salario:.2f}")
print("Parabéns, você recebeu um aumento!")
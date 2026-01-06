#Escreva um progama para aprovar o empréstimo bancário para a compra de uma casa. O progama vai perguntar o valor da casa, o salário do comprador  em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou então o empréstimo seá negado

casa = int(input("Qual o valor da casa? "))
salário = int(input("Qual o seu salário? "))
anos = int(input("Qual a previsão de pagar em até quantos anos? "))

meses = anos * 12
prestação = casa / meses
limite = salário * 0.30

print(f"\nPara pagar uma casa de R${casa:.2f} em {anos} anos:")
print(f"A prestação será de R${prestação:.2f}")

if prestação < limite:
    print(f"Seu empréstimo foi APROVADO!!!, os valores das prestações são de {float(prestação)} ")
else:
    print("O empréstimo foi NEGADO!!")
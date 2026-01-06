#Elabore um Programa que calcula e o valor a ser pago por um produto considerando o seu preço normal e condição de pagamento:

#A vista dinheiro/cheque:10% de desconto 
#Á vista con cartão 5% de desconto
#Em até 2x no cartão prço normal 
#3X pu mais no cartão: 20% de juros

preço = float(input("Qual o preço do produto? "))

print("""
FORMAS DE PAGAMENTO:
[ 1 ] à vista dinheiro/cheque (10% desconto)
[ 2 ] à vista no cartão (5% desconto)
[ 3 ] 2x no cartão (preço normal)
[ 4 ] 3x ou mais no cartão (20% juros)
""")

forma = int(input("Qual é a opção? "))

if forma == 1 :
    total = preço - (preço * 0.10)
    print(f"Sua compra é de R$\033[1;32m{preço:.2f}\033[m vai custar R$\033[1;25m{total:.2f}\033[m no final")
elif forma == 2:
    total = preço - (preço * 0.05)
    print(f"Sua compra é de R$\033[1;32m{preço:.2f}\033[m vai custar R$\033[1;32m{total:.2f}\033[m no final")
elif forma == 3:
    total  = preço
    parcela = total /2
    print(f"Sua compra sera parcelada em  de R$\033[32m{parcela:.2f}\033[m")
elif forma == 4:
    total = preço + (preço * 0.20)
    total_parcelas = int(input("Quantas parcelas? "))
    parcela = total_parcelas / total
    print(f"Sua compra será parcelada em {total_parcelas} x de R${parcela:.2f} Com juro.")
    print(f"Sua compra de R$\033[32m{preço:.2f}\033[m vai custar R$\33[1;32m{total}\033[m no final.")
else:
    print("OPÇÃO INVÁLIDA de pagamento. Tente novamente.")
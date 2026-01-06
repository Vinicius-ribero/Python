#Desenvolva uma lógica que leia o peso e a altura de uma pessoas, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

#Abaixo de 18.5:Abaixo do peso 
#Entre 18.5 e 25: Peso ideal
#25 até 30: Sobrepeso
#30 até 40 :Obesidade
#Acima de 40: Obesidade Mórbida

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura:"))
IMC = peso / (altura ** 2)

print(f"Seu IMC é: {IMC:.2f}")

if IMC < 18.5:
    print("Você está abaixo do peso!")
elif IMC > 18  and IMC <= 25:
    print("Você está no seu peso ideial!")
elif IMC > 25 and IMC <= 30:
    print("Você está com sobrepeso")
elif IMC > 30 and IMC <= 40:
    print("Você está Obeso!")
else: 
    print("Você em Obesidade Mórbida ")
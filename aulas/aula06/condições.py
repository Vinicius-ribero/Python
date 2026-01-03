nome = str(input("Qual é o seu nome?"))
if nome == "Vinicius":
    print("Belo nome que você tem")
else:
    ("Seu nomal é muito comum")
print(f"Bom dia {nome}!")


n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
média = (n1+n2)/2
print(f"A sua média foi {média:.1f}")
if média >= 6.0 :
    print("Sua média foi boa! Parabéns!")
else: 
    print("Sua média foi ruim! Estude Mais!")

#SIMPLIFICADA 

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
média = (n1+n2)/2
print(f"A sua média foi {média:.1f}")
print("Parabéns" if média >=6 else "Estude mais!")
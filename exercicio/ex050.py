#CRIE UM PROGAMA QU ELEIA UMA FRASE QUALQUER E DIGA SE ELA É UM PALÍNDROMO DESCONSIDERANDO OS ESPAÇOS
#APOS A SOPA

frase = str(input("Digite uma frase: ")).strip().upper()#
palavras = frase.split()
junto = "".join(palavras) #JUNTAS TODA A FRASE
inverso = ""
for letra in range(len(junto) -1, -1, -1 ):
    inverso += junto[letra]
print(f"O inverso de {junto} é {inverso}")
if inverso == junto:
    print("Temos um palíndromo!")
else:
    print("A frase digitada não é um palíndromo!")



#FORMA MAIS SIMPLES

frase = str(input("Digite uma frase: ")).strip().upper()#
palavras = frase.split()
junto = "".join(palavras) #JUNTAS TODA A FRASE
inverso = junto [::-1] 
print(f"O inverso de {junto} é {inverso}")
if inverso == junto:
    print("Temos um palíndromo!")
else:
    print("A frase digitada não é um palíndromo!")
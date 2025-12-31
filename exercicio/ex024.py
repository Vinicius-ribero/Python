frase = input("Digite uma frase:")
print(f"A letra aparece {frase.upper().count("A")} vezes na frase")
print(f"A primeira letra A apareceu na posição {frase.find("a")+1}")
print(f"A primeira letra A apareceu na posição {frase.rfind("a")+1}")
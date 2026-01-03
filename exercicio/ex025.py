import random

computador = random.randint(0,100)

chute = int(input("Adivinha o núemro de 0 a 100: "))

if chute == computador:
    print("Você Venceu!")
else: (f"Você perdeu! O computador pensou no {computador} ")
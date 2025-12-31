from random import shuffle
n1 = str(input("Primeiro Aluno"))
n2 = str(input("Segundo Aluno"))
n3 = str(input("Terceiro Aluno"))
n4 = str(input("Quarto Aluno"))

ordem  = [n1, n2 ,n3 ,n4]
shuffle (ordem)

print(f"A odrem de apresentação será {ordem}")
import random 
n1 = str(input("João"))
n2 = str(input("Vinícius"))
n3 = str(input("Gabriel"))
n4 = str(input("Rafael"))

ordem = random.sample([n1, n2, n3, n4], k=4)

print(f"A ordem sorteada dos 4 alunos {ordem}")
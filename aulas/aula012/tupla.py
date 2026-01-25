#TUPLAS

lanche = ["hamburguer", "suco", "pizza", "pudim", "Batata Frita"]

print(lanche)
print("="*20)

print(lanche [2]) #Mostra o número 2 [pizza];
print("="*20)

print(lanche [1:3]) #Mostra um fatiamento de tuplas mostrando [suco] e [pudim]
print("="*20)

print(lanche [1:]) #Mostra do suco [1] para frente;
print("="*20)

print(lanche [:2]) #Mostra de pizza para trás 1] para frente;
print("="*20)


print(lanche [-1]) #Mostra decrecente  ou de trás para frente o -1 seria o pudim;
print("="*20)

print(len (lanche)) # O len mostra quantos item(indices) tem nessa tupla que seria = 4
print("="*20)

for comida in lanche:
    print(f"Eu vou comer {comida}")
print("Comi bastante")

print("="*20)

for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {pos}") # Semelhante ao mesmo for de baixo porém de outro manereira escrita!

print("="*20)

for cont in range(0, len(lanche)):
    print(F"Eu vou comer {lanche [cont]} na posição {cont}") # O for de cima é o mesmo de baixo, porém são utilizadas em meios diferentes

print("="*20)

#SORTED = Mostra a tupla em ordem (alfabetica)

print(sorted(lanche))
print(lanche)

print("="*20)

#Tuplas com números 

a = (2, 5 , 4)
b = (5, 8, 1, 2)
c = a + b   #Juntas as duas tuplas
print(c)


print("="*20)

a = (2, 5 , 4)
b = (5, 8, 1, 2)
c = a + b   
print(len(c)) #Mostra quantas numero possui dentro das tuplas

print("="*20)

a = (2, 5 , 4)
b = (5, 8, 1, 2)
c = a + b   
print(c.count(5)) #Mostra quantos numero 5  possui dentro das tuplas

print("="*20)

#INDEX

a = (2, 5 , 4)
b = (5, 8, 1, 2)
c = b + a   
print(c)
print(c.index(8)) #O index vai mostrar em que posição está o numero 8

print("="*20)

#APAGANDO TUPLA
pessoa = ("Gustavo", 39, "M", 99.98)
del(pessoa)
print(pessoa)




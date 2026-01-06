#Refaça o DESAFIO ex032 dos triângulos acrecescentando o recurso de mostar que tipo e triângulo será formado:

#Equilátero: todos os lados iguai
#Isósceles: dois lados iguais 
#Escaleno todos os lados diferentes

print("-=" * 20)
print("Analisador de Triângulos v2.0")
print("-=" * 20)

r1 = float(input("Primeiro Segmento: "))
r2 = float(input("Segundo Segmento: "))
r3 = float(input("Terceiro Segmento: "))

# 1. Verifica se os segmentos podem formar um triângulo
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima PODEM FORMAR um triângulo ", end="")
    
    # 2. Estrutura aninhada para identificar o tipo
    if r1 == r2 == r3:
        print("EQUILÁTERO!")
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print("ESCALENO!")
    else:
        print("ISÓSCELES!")

else:
    print("Os segmentos acima NÃO PODEM FORMAR um triângulo!")

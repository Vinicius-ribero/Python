for c in range(1, 7):
    print(c)
print("FIM")

# FAZ UMA CONTAGEM DESCRENTE
for c in range(6, 0, -1):
    print(c)
print("FIM")

# FAZ UM CONTAGEM ATÉ 6 PORÉM PULANDO DE DOIS EM DOIS
for c in range(0 ,7, 2):
    print(c)
print("FIM")

n = int(input("Digite um número: "))
for c in range(0, n+1):
    print(c)

i = int(input("Ínicio: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
for c in range(i, f+1, p):
    print(c)

for c in range(0,3):
    n = int(input("Digite um valor: "))
print("FIM")

s = 0
for c in range(0,3):
    n = int(input("Digite um valor: "))
    s = s + n
print(f"O somatório de todos os valores foi {s}")
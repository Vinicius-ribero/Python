#Faça uma taboada de um núemro que o usuário escolher, só que agora utilizando um laço for.

num = int(input("Digite um número: "))
print("-=" * 10)
for c in range(1, 11):
    tabuada = num * c
    print(f"Tabuada de {num} x {c} = {tabuada}")

print("-=" *10)
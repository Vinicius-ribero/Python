#Crie um progama onde usuário possa digitar cinco valores númericos e cadastre-os em uma lista, já na posição correta de inserção
#Sem usar o sort().
#No final mostre a lista ordenada na tela 

lista = []

for c in range(0,5):
    valores = int(input("Digite um valor: "))
    if c == 0 or valores > lista[-1]:
        print("Adicionado ao final da lista.....")
    else:
        pos = 0
        while pos < len(lista):
            if valores <lista[pos]:
                rpin5




#Crie um progama que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta.No final mostre um boletim contenco a média de cada um e permita que o usuario possa mostrar as notas de cada aluno individualmente.


ficha = list()
while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])

    res = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if res == "N":
        break

print("-=" * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print("-" * 26)

for i, a in enumerate(ficha):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")

while True:
    print("-" * 35)
    opc = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    
    if opc == 999:
        print("FINALIZANDO...")
        break
    
    # Verificação de segurança para o índice
    if 0 <= opc < len(ficha):
        print(f"Notas de {ficha[opc][0]} são {ficha[opc][1]}")
    else:
        print("Opção inválida! Tente novamente.")

print("<<< VOLTE SEMPRE >>>") 
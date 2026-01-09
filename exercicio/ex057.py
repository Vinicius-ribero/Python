#REFAÇA O DESADIO 051, LENDO O PRIMEIRO TERMO E A RAZAÃO DE UMA PA, MOSTRNADO OS 10 PRIMEIROS TERMOS DA PROGRESSÃO USANDO A ESTRUTURA WHILE

primeiro = int(input("Digite o primeiro termo: "))
razão = int(input("Razão: "))

termo = primeiro
cont = 1

while cont <= 10:
    print(f"{termo} → ", end="")
    termo += razão
    cont += 1

print("FIM"),
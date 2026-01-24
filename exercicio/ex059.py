#Escreva um progama que leia um número n inteiro qualquer n=e mostre na tela os n primerios elementos de uma sequêcnia de fibonacci 

# Passo 1: Ler quantos termos o usuário deseja
n = int(input("Quantos termos você quer mostrar? "))

# Passo 2: Definir os dois primeiros termos (base da sequência)
t1 = 0
t2 = 1

print("~" * 30)
print(f"{t1} → {t2}", end=" ")

# Passo 3: Configurar o contador
# Como já mostramos os 2 primeiros termos, o contador começa no 3
cont = 3

# Passo 4: O laço de repetição
while cont <= n:
    t3 = t1 + t2           # Calcula o novo termo (soma dos dois anteriores)
    print(f"→ {t3}", end=" ")
    
    # A "Dança das Variáveis" (Passagem de bastão)
    t1 = t2                # O t1 passa a ser o que era o t2
    t2 = t3                # O t2 passa a ser o novo valor (t3)
    
    cont += 1              # Incrementa o contador

print("→ FIM")
print("~" * 30)

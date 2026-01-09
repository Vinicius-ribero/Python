#Desenvolva um porgama que leia o primeiro termo e  a razaão de uma PA. no final mostre os 10 primeiros termos dessa progressão.

primeiro = int(input("Digite o primeiro termo: "))
razão = int(input("razão: "))
decimo = primeiro + (10 - 1) * razão

for c in range(primeiro,decimo + razão , razão):
    print(c)

print('ACABOU')
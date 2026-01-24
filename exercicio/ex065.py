from random import randint

print("=-"*20)
print(f"VAMOS JOGAR PAR OU ÍMPAR")
print("=-"*20)

vitorias = 0

while True:
    jogador = int(input("Diga um valor: "))
    # Corrigi a posição dos parênteses do input aqui:
    escolha = str(input("Par ou Ímpar? [P/I] ")).upper().strip()[0]
    
    computador = randint(0, 10)
    total = computador + jogador
    
    if total % 2 == 0:
        resultado_real = "PAR"
    else:
        resultado_real = "IMPAR"
        
    print("-" * 20)
    print(f"Você jogou {jogador} e o computador {computador}. Total de {total} DEU {resultado_real}")
    print("-" * 20)

    # Verificação de vitória ou derrota
    if escolha == 'P':
        if resultado_real == 'PAR':
            print("VOCÊ VENCEU!")
            vitorias += 1
        else:
            print("VOCÊ PERDEU!")
            break
    elif escolha == 'I':
        if resultado_real == 'IMPAR':
            print("VOCÊ VENCEU!")
            vitorias += 1
        else:
            print("VOCÊ PERDEU!")
            break
    else:
        print("Opção inválida! Escolha P ou I.")
        continue # Faz o loop voltar ao início se digitar errado

    print("Vamos jogar novamente...")
    print("=-" * 20)

print(f"FIM DE JOGO! Você conquistou {vitorias} vitória(s) consecutiva(s).")

#/033[0:33:4m

#STYLE : 0 = NONE
# 1 = BOLD
# 4 = UNDERLINE
# 7 = NEGATIVE

#TEXT: 
# 30 = WHITE/ BARNCO
# 31 = RED / VERMELHO
# 32 = GREEN  / VERDE
# 33 = YELLOW / AMARELO
# 34 = BLUE / AZUL
# 35 = MAGENTA
# 36 = CYAN / CIANO
# 37 = GRAY / CINZA

#BACKGROUND
# 40 = WHITE/ BARNCO
# 41 = RED / VERMELHO
# 42 = GREEN  / VERDE
# 43 = YELLOW / AMARELO
# 44 = BLUE / AZUL
# 45 = MAGENTA
# 46 = CYAN / CIANO
# 47 = GRAY / CINZA

# print("\033[1;30;41m TESTE \033[m")
# print("\033[4;33;46m TESTE \033[m")
# print("\033[1;35;43m TESTE \033\033[m")
# print("\033[30;42m TESTE \033\033[m")
# print("\033[m TESTE \033\033[m")
# print("\033[7;30m TESTE \033\033[m")



a = 3
b = 5
print(f"Os valores são \033[32m{a} e \033[31m{b}\033[m")

nome = "Vinícius"
cores = {
    "limpa": "\033[m",
    "azul": "\033[34m",
    "amarelo": "\033[33m",
    "preto_branco": "\033[7;30m"
}

# A forma correta é colocar a cor, depois o nome, e depois limpar a cor
print(f"Olá muito prazer em te conhecer {cores['amarelo']}{nome}{cores['limpa']}")
print(f"Olá muito prazer em te conhecer {cores['azul']}{nome}{cores['limpa']}")
print(f"Olá muito prazer em te conhecer {cores['limpa']}{nome}{cores['limpa']}")
print(f"Olá muito prazer em te conhecer {cores['preto_branco']}{nome}{cores['limpa']}")
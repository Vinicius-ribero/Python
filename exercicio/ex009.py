# Passo 1: Entrada de dados
largura = float(input("Digite a largura da parede (em metros): "))
altura = float(input("Digite a altura da parede (em metros): "))

# Passo 2: Cálculo da área (Largura x Altura)
area = largura * altura

# Passo 3: Cálculo da tinta (Cada litro pinta 2 metros quadrados)
tinta = area / 2

# Exibição dos resultados
print("-" * 30)
print(f"Sua parede tem a dimensão de {largura}x{altura} e sua área é de {area:.2f}m².")
print(f"Para pintar essa parede, você precisará de {tinta:.2f}l de tinta.")
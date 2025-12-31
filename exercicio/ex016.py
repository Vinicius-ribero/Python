import math

# Entrada de dados
ângulo_graus = float(input("Digite o valor do ângulo em graus = "))

# Conversão necessária: Graus para Radianos
ângulo_rad = math.radians(ângulo_graus)

# SENO
print(f"O seno de {ângulo_graus}° é igual a {math.sin(ângulo_rad):.2f}")

# COSSENO
print(f"O cosseno de {ângulo_graus}° é igual a {math.cos(ângulo_rad):.2f}")

# TANGENTE
print(f"A tangente de {ângulo_graus}° é igual a {math.tan(ângulo_rad):.2f}")
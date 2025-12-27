algo = input("Digite um valor:")
print(F"O tipo primitivo deste elemento é {type (algo)}")

## Usando os métodos 'is' para obter informações

print(f"Só tem espaços? {algo.isspace()}")
print(f"É um número? {algo.isnumeric()}")
print(f"É alfabético (letras)? {algo.isalpha()}")
print(f"É alfanumérico (letras ou números)? {algo.isalnum()}")
print(f"Está em maiúsculas? {algo.isupper()}")
print(f"Está em minúsculas? {algo.islower()}")
print(f"Está capitalizada (primeira letra maiúscula)? {algo.istitle()}")
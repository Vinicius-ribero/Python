#PADRÃO
import math
ca = float(input("Digite o cateto adjancente do triângulo retângulo :"))
co = float(input("Digite o cateto oposto do triângulo retãngulo:"))
comprimento_hipotenusa = int(ca ** 2)+ (co **2)
print(f"O comprimento do cateto adjacenet {ca} e o cateto oposto {co} seu valor calculado pfloatara a hipotenusa é de  {float(int(math.sqrt(comprimento_hipotenusa)))}")

#MODO HYPOT
from math import hypot
ca = float(input("Digite o cateto adjancente do triângulo retângulo :"))
co = float(input("Digite o cateto oposto do triângulo retãngulo:"))
hi = hypot(co, ca)
print(f"A hipotenusa vai medir {hi:.2f}")
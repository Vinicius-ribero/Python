import math
ca = int(input("Digite o cateto adjancente do triângulo retângulo :"))
co = int(input("Digite o cateto oposto do triângulo retãngulo:"))
comprimento_hipotenusa = int(ca ** 2)+ (co **2)
print(f"O comprimento do cateto adjacenet {ca} e o cateto oposto {co} seu valor calculado para a hipotenusa é de  {int(math.sqrt(comprimento_hipotenusa))}")
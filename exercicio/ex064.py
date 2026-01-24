#FAÇA UM PROGAMA QUE MOSTRE A TABUADA DE VÁRIOS NUMERO, UM DE CADA VEZ, PARA CADA VALor DIGITADO PELO USUÁRIO. O PROGAMA SERÁ INTERROMPIDO QUANDO O NUMERO SOLICITADO FOR NEGATIVO 



# n = cont =   0

# while True:
#     n = int(input("Quer ver a Tabuada de qual valor? "))
#     resul1 = (n* 1)
#     resul2 = (n* 2)
#     resul3 = (n* 3)
#     resul4 = (n* 4)
#     resul5 = (n* 5)
#     resul6 = (n* 6)
#     resul7 = (n* 7)
#     resul8 = (n * 8)
#     resul9 = (n * 9)
#     resul10 = (n * 10)
#     print("-"*20)
#     print(f"{n} x 1 =  {resul1}")
#     print(f"{n} x 2 =  {resul2}")
#     print(f"{n} x 3 =  {resul3}")
#     print(f"{n} x 4 =  {resul4}")
#     print(f"{n} x 5 =  {resul5}")
#     print(f"{n} x 6 =  {resul6}")
#     print(f"{n} x 7 =  {resul7}")
#     print(f"{n} x 8 =  {resul8}")
#     print(f"{n} x 9 =  {resul9}")
#     print(f"{n} x 10 = {resul10}")
#     cont += 1
#     if n  <= -1:
#         print("PROGRAMA TABUADA ENCERRADO. Volte Sempre")
#     print("-"*20)
print("-"*20)
while True:
    n = int(input("Quer ver a tabuada e qual valor? "))

    if n <= -1:
        break
    elif n == 0:
        break
    else:
        for c in range(1, 11):
            print(f"{n} x {c} = {n * c}")    
    print("-"*20)
print("PROGRAMA TABUADA ENCERRADO. Volte Sempre!")
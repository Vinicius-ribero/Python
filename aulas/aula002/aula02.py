n1 = int(input("Digite um valor:"))
n2 = int(input("Digite outro:"))
soma = n1+ n2
print(f"A soma entre {n1 , n2}  é igual o resultado =  {soma}")

n = float(input("Digite um valor:"))
print(n) # CONVERTE PARA DECIMAL 

n = bool(input("Digite um valor:"))
print(n) #MOSTRA VERDADEIRO SE COLOCAR UM NÚMERO  OU FALSO SE NÃO COLOCAR NENHUM NÚMERO 

#IS
n = input("Digite algo:")
print(n.isnumeric()) #VERIFICA SE O ELEMENTO DIGITADO É NUMMÉRICO


n = input("Digite algo:")
print(n.isalpha()) #VERIFICA SE HÁ UMA STRING E SE FOR NÚMERO É FALSO 












# int (Inteiro)
# O int (abreviação de integer) é usado para números inteiros, ou seja, números que não possuem vírgula ou casas decimais. Eles podem ser positivos ou negativos.

# Exemplos: 10, -5, 1000, 0.

# Uso comum: Contar itens (como 3 laranjas), idade de uma pessoa ou o ano atual.

# FLOAT (Flutuante)
# O float é usado para números decimais. O nome vem de "ponto flutuante", porque no Python usamos um ponto . em vez de vírgula para separar as casas decimais.c

# Exemplos: 5.99, -1.5, 10.0 (mesmo sendo um número "inteiro" visualmente, o .0 o torna um float).

# Uso comum: Preços de produtos, altura, peso ou qualquer medida precisa.

#  STR (String)
# A str (abreviação de string, que significa "cordão" ou "sequência") é usada para textos. Tudo o que estiver dentro de aspas (simples ' ' ou duplas " ") o Python entende como uma string.

# Exemplos: "Olá Mundo", 'Python', "123" (aqui o 123 é tratado como texto, não como número).

# Uso comum: Nomes de usuários, mensagens, endereços de e-mail.

# BOOL(Booleano)
# O bool (em homenagem a George Boole) é o tipo mais simples: ele só aceita dois valores: Verdadeiro ou Falso. É como um interruptor de luz.

# Valores: True (Verdadeiro) ou False (Falso). Note que em Python a primeira letra deve ser sempre maiúscula.

# Uso comum: Verificações de segurança (Está logado? Sim/Não), sensores ou perguntas lógicas.
#Crie um progama que tenha uma tiupla com várias palvaras(não usar acentos) Depois disso, você deve mostrar, para cada palavra quais, são suas vogais.

palavras = ("aprender", "progamar", "linguagem", "Python", "curso", "gratis", "estudar", "praticar", "trabalhar", "mercado", "progamador", "futuro")

for p in palavras:
   print(f"\nNa palavra {p.upper()} temos: ", end="")
   for letra in p:
         if letra.lower() in "aeiou":
              print(letra, end= "")
 
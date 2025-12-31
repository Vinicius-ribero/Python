#FRASE "Curso em Vídeo Python";
#len(frase) > QUAL O COMPRIMENTO DA FRASE?;
#frase.count("o") MOSTRA QUAL VEZES POSSUI A LETRA NO PARÊNTESES NO CASO A LETRA O ;
#frase.count("o",0,13) MOSTRA ENTREOS CARCTERES 0 POSUUI APENAS UMA LETRA "O";
#frase.find("deo")MOSTRA ENTRE OS PARENTÊSES A PARTE SELECIONADA DA FRASE;
#frase.find("Android") RESULTADO MOSTRA -1;
#Curso in Frase;
#frase.replace("Python", "Android") SUBISTITUI A PALAVAR PYTHON POR ANDROID = "CURSO EM VIDEO ANDROID";
#frase.upper() TRANSFORMA A FRASE TODA EM MAIÚSCULA "CURSO EM VÍDEO PYTHON";
#frase.lower() TRANSFORMA AS FRASE TODA EM MINÚSCULA "curso em vídeo python";
#frase.capitalize() COLOCA TODOS OS CARACTERES EM MINÚCLAS MENOS O PRIMEIRO CARACTERE = "Curso em vídeo python"
#frase.title() ANALISA QUANTAS PALAVRAS TEM A STRING E E TRANSFORMA AS PRIMEIRA CARCTERES EM MAIÚSCULA =Curso Em Vídeo Python
#frase.strip() VAI REMOVER "x" 'OS PRIMEIROS ESPAÇOS E ULTIMOS DE UMA STRING = xxx"Aprenda Python"xx
#frase.split() DIVIDE AS PALAVRAS REINICIANDO SEUS ÍNDICE = Cu¹r²s³o  em¹ ví¹d²e³o  Py¹t²h³on
#"-".join(frase) FAZ UMA JUNÇÃO NOS ESPAÇOS DA FRASE = Curso-em-Vídeo-Python

frase = "Curso em Vídeo Python"
print(frase[3])#SELECIONA O INDICE NUMERO 3(S)
print(frase[3:13])#SELECIONA DO INDICE 3(S) ATÉ O INDICE 13(E)
print(frase[:13])# SELECIONA ATÉ O INDICE13 = CURSO EM VÍDE
print(frase[1:15])# SELECIONA DO INDICE1 ATÉ O INDICE15 = urso em Vídeo
print(frase[1:15:2])#SELECIONA DO  INDICE 1 ATÉ O INDICE15 PORÉM PULANDO DE 2 EM 2 = us mVdo
print(frase[1::2])#SELECIONA DO INIDICE 1 ATÉ O FINAL DA STRING PULANDO DE 2 EM 2 = us mVdoPto
print(frase.count("o"))#CONTA QUANTAS "o" tem na frase
print(frase.upper().count("O"))#CONTA TODAS OS "O" MAIÚSCULOS NA STRING
print(len(frase)) #FAZ UM CONTAGEM DA DOS INDICES DA FRASE
print(frase.lower())
print(frase.find("vídeo"))
print(frase.split())

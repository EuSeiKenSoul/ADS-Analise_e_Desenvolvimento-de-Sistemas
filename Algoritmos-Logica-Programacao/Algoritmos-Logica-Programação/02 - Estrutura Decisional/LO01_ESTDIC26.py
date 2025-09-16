#Lote 1.1
'''
LO01_ESTDIC26
Receba 2 números inteiros. Verifique e mostre se o maior número é múltiplo do menor. 

'''
###################################################################################



print("Este programa verifica se o número maior é divisivel pelo número menor.")
print("================================================================================================================================")
#declarando variavel e recebendo valores/dados

numUm = int(input(f'Digite um número: '));
numDois = int(input(f'Digite outro número: '));

#Solucionando problema ou realizando calculos


if (numUm > numDois):#DEfinir qual é o número maior
    numMaior = numUm;
    numMenor = numDois;
else:
    numMaior = numDois;
    numMenor = numUm;

#verificar se o número maior é divisivel pelo número menor usando uma variavel booleana visando futuramente reutilização de codigos.
if (numMaior % numMenor == 0):
    varBool = True;
else:
    varBool = False;

#Apresentação de resultados

if (varBool == True):
    print(f'O Número {numMaior} é divisivel por {numMenor}');
else:
    print(f'O Número {numMaior} Não é divisivel por {numMenor}');

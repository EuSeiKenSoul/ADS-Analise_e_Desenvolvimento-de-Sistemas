#Lote 1.1
'''
LO01_ESTDIC18
Receba 2 valores inteiros. Calcule e mostre o resultado da diferença do 
maior pelo menor valor. 


'''




print("Este programa calcula e mostre o resultado da diferença do maior pelo menor valor.")
print("===========================================================================================================")
#declarando variavel e recebendo valores
numUm = int(input("Digite um valor:  "));
numDois = int(input("Digite ouro valor:  "));




#Solucionando problema ou realizando calculos
if (numUm > numDois) :
    result = (numUm - numDois);
    print("====================================================")
    print (f'{numUm} é maior que {numDois} por {result}');
else:
    result = (numDois - numUm);
    print("====================================================")
    print (f'{numDois} é maior que {numUm} por {result}');

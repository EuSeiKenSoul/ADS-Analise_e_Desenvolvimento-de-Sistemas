#Lote 1.1
'''
LO01_ESTDIC18
Receba 2 valores inteiros. Calcule e mostre o resultado da diferença do 
maior pelo menor valor. 


'''
print("Este programa calcula e mostre o resultado da diferença do maior pelo menor valor.")
print("===========================================================================================================")

#Solucionando problema ou realizando calculos
def Mostra_Diferenca():
    if (numUm > numDois) :
        result = (numUm - numDois);
        print("====================================================")
        print (f'{numUm} é maior que {numDois} por {result}');
    else:
        result = (numDois - numUm);
        print("====================================================")
        print (f'{numDois} é maior que {numUm} por {result}');


#declarando variavel e recebendo valores
numUm = int(input("Digite um número:  "));
while numUm <=0 :
    print(f'Valor inválido, digite um valor maior que zero')
    numUm = int(input("Digite um número"))

numDois = int(input("Digite outro número:  "));
while numDois <=0 :
    print(f'Valor inválido, digite um valor maior que zero')
    numDois = int(input("Digite um número"))

Mostra_Diferenca()
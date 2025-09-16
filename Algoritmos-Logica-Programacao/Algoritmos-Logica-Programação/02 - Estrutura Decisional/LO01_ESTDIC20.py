#Lote 1.1
'''
LO01_ESTDIC20
Receba 3 coeficientes A, B e C de uma equação do 2º grau da fórmula 
AX²+BX+C=0. Verifique e mostre a existência de raízes reais e se caso 
exista, calcule e mostre. 


'''




print("Este programa compara dois valores e mostra o maior deles.")
print("===========================================================================================================")
#declarando variavel e recebendo valores
numUm = float(input("Digite um valor:  "));
numDois = float(input("Digite ouro valor:  "));




#Solucionando problema ou realizando calculos
if (numUm > numDois) :
    
    print("====================================================")
    print (f'{numUm:.2f} é maior que o número {numDois:.2f}');
else:
    
    print("====================================================")
    print (f'{numDois:.2f} é maior que o número {numUm:.2f}');

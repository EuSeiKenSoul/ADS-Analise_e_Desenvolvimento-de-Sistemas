#Lote 1.1
'''
LO01_ESTDIC19
Receba 2 valores reais. Calcule e mostre o maior deles.


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

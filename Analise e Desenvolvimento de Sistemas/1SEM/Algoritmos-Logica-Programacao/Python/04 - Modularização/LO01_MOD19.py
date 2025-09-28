#Lote 1.1
'''
LO01_ESTDIC19
Receba 2 valores reais. Calcule e mostre o maior deles.


'''
print("Este programa compara dois valores e mostra o maior deles.")
print("===========================================================================================================")





#Solucionando problema ou realizando calculos
def Mostra_Diferenca():
    if (numUm > numDois) :
        
        print("====================================================")
        print (f'{numUm:.2f} é maior que o número {numDois:.2f}');
    else:
        
        print("====================================================")
        print (f'{numDois:.2f} é maior que o número {numUm:.2f}');



#declarando variavel e recebendo valores
numUm = float(input("Digite um número:  "));
while numUm <=0 :
    print(f'Valor inválido, digite um valor maior que zero')
    numUm = float(input("Digite um número"))

numDois = float(input("Digite outro número:  "));
while numDois <=0 :
    print(f'Valor inválido, digite um valor maior que zero')
    numDois = float(input("Digite um número"))

Mostra_Diferenca()
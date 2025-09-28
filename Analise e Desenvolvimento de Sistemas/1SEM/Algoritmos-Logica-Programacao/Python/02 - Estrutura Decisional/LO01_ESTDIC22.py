#Lote 1.1
'''
LO01_ESTDIC21
Receba 2 valores inteiros e diferentes. Mostre seus valores em ordem 
crescente.

'''
###################################################################################



print("Este programa organiza dois números em ordem crescente.")
print("================================================================================================================================")
#declarando variavel e recebendo valores
numUm = int(input("Digite o primeiro número:  "));
numDois = int(input("Digite o segundo número:  "));




#Solucionando problema ou realizando calculos

if(numUm < numDois):
    print(f'{numUm}, {numDois}');
elif(numDois < numUm):
    print(f'{numDois}, {numUm}');
else:
    print('Nenhum número é maior que o outro, portanto os números são iguais.');


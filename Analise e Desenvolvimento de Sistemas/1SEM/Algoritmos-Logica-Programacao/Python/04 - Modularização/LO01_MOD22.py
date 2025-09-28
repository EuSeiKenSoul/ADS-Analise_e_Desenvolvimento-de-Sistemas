#Lote 1.1
'''
LO01_ESTDIC22
Receba 2 valores inteiros e diferentes. Mostre seus valores em ordem 
crescente.

'''
###################################################################################
#MODULOS

def ordenar_crescente():#Ordena dois número em ordem crescente
    if(numUm < numDois):
        numOrdUm = numUm
        numOrdDois= numDois
        
    elif(numDois < numUm):
        numOrdUm = numDois
        numOrdDois= numUm
    print(f'\n\nNúmeros ordenados abaixo:\n')
    print(f'{numOrdUm}, {numOrdDois}\n\n')


print("Este programa organiza dois números em ordem crescente.")
print("================================================================================================================================")
#declarando variavel e recebendo valores
numOrdUm = 0
numOrdDois = 0
numUm = int(input("Digite o primeiro número:  "))
while numUm < 0:
    print(f'O número não pode ser negativo!')
    numUm = int(input("Digite o primeiro número:  "))

numDois = int(input("Digite o segundo número:  "))
while numDois < 0 or numDois == numUm:
    if numDois < 0 :
        print(f'O número não pode ser negativo!')
    elif numDois == numUm:
        print(f'O número não pode ser igual a {numUm} que é o primeiro número fornecido!')
    numDois = int(input("Digite o segundo número:  "))

ordenar_crescente()




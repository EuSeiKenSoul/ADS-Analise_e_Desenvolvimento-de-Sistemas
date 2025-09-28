#Lote 1.1
'''
LO01_ESTDIC23
Receba 3 valores obrigatoriamente em ordem crescente e um 4º valor não 
necessariamente em ordem. Mostre os 4 números em ordem crescente. 

'''
###################################################################################
#MODULOS

def ordenar_crecente_quatro():
    if numQuatro < numUm  :
        numOrdUm = numQuatro
        numOrdDois = numUm
        numOrdTres = numDois
        numOrdQuatro = numTres
    elif numQuatro > numUm and numQuatro < numDois :
        numOrdUm = numUm
        numOrdDois = numQuatro
        numOrdTres = numDois
        numOrdQuatro = numTres
    elif numQuatro > numDois and numQuatro < numTres :
        numOrdUm = numUm
        numOrdDois = numDois
        numOrdTres = numQuatro
        numOrdQuatro = numTres
    elif numQuatro > numTres :
        print(f'{numUm}, {numDois}, {numTres} e {numQuatro}')
        numOrdUm = numUm
        numOrdDois = numDois
        numOrdTres = numTres
        numOrdQuatro = numQuatro
    print(f'Os números em ordem crescente são:{numOrdUm}, {numOrdDois}, {numOrdTres} e {numOrdQuatro}')


print("Este programa organiza 4 números em ordem crescente.")
print("================================================================================================================================")
#declarando variavel
numUm = 0
numDois = 0
numTres = 0
numQuatro = 0
numOrdUm = 0
numOrdDois = 0
numOrdTres = 0
numOrdQuatro = 0

#entrada de valores
numUm = int(input(f'Digite o primeiro número:  '))
while numUm <=0:
    print(f'Número não pode ser negativo!')
    numUm = int(input(f'Digite o primeiro número:  '))

numDois = int(input(f'Digite o segundo número:  '))
while numDois <= numUm :
    print(f'O Segundo número de ser maior que {numUm}!')
    numDois = int(input(f'Digite o segundo número:  '))

numTres = int(input(f'Digite o terceiro número:  '))
while numTres <= numDois :
    print(f'O Terceiro número de ser maior que {numDois}!')
    numTres = int(input(f'Digite o terceiro número:  '))

numQuatro = int(input(f'Digite o quarto número:  '))

#invocando modulo
ordenar_crecente_quatro()
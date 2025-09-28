#Lote 1.1
'''
LO01_ESTDIC21
Receba 3 valores obrigatoriamente em ordem crescente e um 4º valor não 
necessariamente em ordem. Mostre os 4 números em ordem crescente. 

'''
###################################################################################



print("Este programa organiza 4 números em ordem crescente.")
print("================================================================================================================================")
#declarando variavel e recebendo valores

numUm = int(input("Digite o primeiro número:  "));
numDois = int(input(f'Digite o segundo número, ele deve ser maior que {numUm}:  '));
while numDois <= numUm :
    numDois = int(input(f'Digite o segundo número, ele deve ser meior que {numUm}:  '));

numTres = int(input(f'Digite o terceiro número, ele deve ser maior que {numDois}:  '));
while numTres <= numDois :
    numTres = int(input(f'Digite o terceiro número, ele deve ser maior que {numDois}:  '));

numQuatro = int(input(f'Digite o quarto número:  '));



#Solucionando problema ou realizando calculos


if numQuatro < numUm  :
    print(f'{numQuatro}, {numUm}, {numDois} e {numTres}');
elif numQuatro > numUm and numQuatro < numDois :
    print(f'{numUm}, {numQuatro}, {numDois} e {numTres}');
elif numQuatro > numDois and numQuatro < numTres :
    print(f'{numUm}, {numDois}, {numQuatro} e {numTres}');
elif numQuatro > numTres :
    print(f'{numUm}, {numDois}, {numTres} e {numQuatro}');
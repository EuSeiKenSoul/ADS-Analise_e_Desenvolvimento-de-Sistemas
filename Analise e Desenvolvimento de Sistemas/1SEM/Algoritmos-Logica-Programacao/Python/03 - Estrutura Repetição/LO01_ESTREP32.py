#Lote 1.1
'''
LO01_ESTREP32
Receba um número inteiro. Calcule e mostre o seu fatorial. 


'''
print("Este programa rececbe um número inteiro, Calcula e mostra o seu fatorial. ")
print("===========================================================================================================")
#declarando variavel e recebendo valores
numA = int(input("Digite um número inteiro: "));
fatoA = numA;
fatoAbk = numA;
#processamento
while numA != 1:
    numA = numA - 1;
    fatoA = fatoA * numA;
#saida
print("O fatorial de",fatoAbk,"é igual a",fatoA);
print("===========================================================================================================")    
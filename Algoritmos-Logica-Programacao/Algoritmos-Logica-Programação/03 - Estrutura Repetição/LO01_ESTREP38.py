#Lote 1.1
'''
LO01_ESTREP38
Receba 100 números inteiros reais. Verifique e mostre o maior e o menor valor. Obs.: somente valores positivos. 


'''
print("Este programa Recebe 100 números inteiros reais. Verifique e mostre o maior e o menor valor. Obs.: somente valores positivos. ")
print("===========================================================================================================")
# declarando variável e recebendo valores e validando entrada de dados
numN = int(input("Digite um número: "))
i = 0
while numN <= 0:
    print("Número inválido! Digite um número maior que zero.")
    numN = int(input("Digite um número: "))

while numN > 0:
    maior = numN
    menor = numN
    while i < 99:
        numN = int(input("Digite outro número: "))
        while numN <= 0:
            print("Número inválido! Digite um número maior que zero.")
            numN = int(input("Digite outro número: "))
        if numN > maior:
            maior = numN
        if numN < menor:
            menor = numN
        i += 1
    break
# mostrando o resultado

print(f'O maior número é {maior} e o menor número é {menor}.')




#Pausa o programa para apresentar o resultado
print("Aperte ENTER para finalizar...")
input()  # Aguarda o usuário pressionar ENTER

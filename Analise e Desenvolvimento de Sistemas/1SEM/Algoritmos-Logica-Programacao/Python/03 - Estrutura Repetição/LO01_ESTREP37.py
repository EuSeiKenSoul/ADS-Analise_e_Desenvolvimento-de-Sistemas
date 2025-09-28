#Lote 1.1
'''
LO01_ESTREP37
Receba um número inteiro. Calcule e mostre a série de Fibonacci até o seu N’nésimo termo. 


'''
print("Este programa recebe um número, calcule e mostra a série 1 + 1/1! + 1/2! + ... + 1/N!")
print("===========================================================================================================")
# declarando variável e recebendo valores e validando entrada de dados
numN = int(input("Digite um número: "))
while numN <= 0:
    print("Número inválido! Digite um número maior que zero.")
    numN = int(input("Digite um número: "))

# calculando a série de Fibonacci
fibo1 = 0
fibo2 = 1
print(f'Série de Fibonacci até o {numN}º termo:')
i = 0
#calculando a série de Fibonacci
while i < numN:
    print(f'{fibo1}', end=' ')
    proximoTermo = fibo1 + fibo2
    fibo1 = fibo2
    fibo2 = proximoTermo
    i += 1
print()  # Quebra de linha após a série
print("===========================================================================================================")





#Pausa o programa para apresentar o resultado
print("Aperte ENTER para finalizar...")
input()  # Aguarda o usuário pressionar ENTER

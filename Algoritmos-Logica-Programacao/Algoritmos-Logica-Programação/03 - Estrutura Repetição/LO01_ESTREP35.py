#Lote 1.1
'''
LO01_ESTREP35
Receba 2 números inteiros, verifique qual o maior entre eles. Calcule e 
mostre o resultado da somatória dos números ímpares entre esses valores. 


'''
print("Este programa recebe verifica qual o maior entre os dois e somas os números ímpares entre eles.")
print("===========================================================================================================")
# declarando variável e recebendo valores
numA = int(input("Digite um número: "))
numB = int(input("Digite outro número: "))

#comparando maior e menos

if numA > numB:
    maior = numA
    menor = numB
else:
    maior = numB
    menor = numA

# Somando os números ímpares entre os dois valores
soma = 0
i=menor
while i <= maior:
    if i % 2 != 0:
        soma += i
    i += 1
print(f"O número {maior} é maior quee {menor} e a soma dos números ímpares entre {menor} e {maior} é: {soma}")
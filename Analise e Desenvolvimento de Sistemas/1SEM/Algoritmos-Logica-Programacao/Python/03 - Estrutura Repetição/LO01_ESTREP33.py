#Lote 1.1
'''
LO01_ESTREP33
Receba um número inteiro. Calcule e mostre o seu fatorial. 


'''
print("Este programa recebe um número inteiro positivo N e calcula a série 1 + 1/2 + 1/3 + ... + 1/N.")
print("===========================================================================================================")

# declarando variável e recebendo valores
numA = int(input("Digite um número inteiro positivo: "))
resultA = 1
i = 2


while numA <= 0:
    print("Número inválido! Digite um número inteiro positivo.")
    numA = int(input("Digite um número inteiro positivo: "))

# processamento
while i <= numA:
    resultA += (1 / i)
    i += 1
print(f"O resultado da série é: {resultA}")

#Lote 1.1
'''
LO01_ESTREP36
Receba um número N. Calcule e mostre a série 1 + 1/1! + 1/2! + ... + 1/N!


'''
print("Este programa recebe um número, calcule e mostra a série 1 + 1/1! + 1/2! + ... + 1/N!")
print("===========================================================================================================")
# declarando variável e recebendo valores e validando entrada de dados
numN = int(input("Digite um número: "))
while numN <= 0:
    print("Número inválido! Digite um número maior que zero.")
    numN = int(input("Digite um número: "))

# Calculando a série
soma = 1.0
fatorial = 1

while fatorial <= numN:
    soma += 1 / fatorial
    fatorial += 1
print(f"A soma da série 1 + 1/1! + 1/2! + ... + 1/{numN}! é: {soma:2.4f}")



#Pausa o programa para apresentar o resultado
print("Aperte ENTER para finalizar...")
input()  # Aguarda o usuário pressionar ENTER

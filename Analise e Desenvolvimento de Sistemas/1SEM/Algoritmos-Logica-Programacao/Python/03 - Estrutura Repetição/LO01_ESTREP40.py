# Lote 1.1
'''
LO01_ESTREP40
Receba 2 números inteiros. Verifique e mostre todos os números primos existentes entre eles. 
'''

print("Este programa recebe dois números e calcula os números primos entre eles:")
print("===========================================================================================================")
numA = int(input("Digite o primeiro número inteiro: "))
while numA <= 0:
    print(f'O número {numA} é inválido. Digite um número inteiro positivo!')
    numA = int(input("Digite o primeiro número inteiro: "))
numB = int(input("Digite o segundo número inteiro: "))
while numB <= 0:
    print(f'O número {numB} é inválido. Digite um número inteiro positivo!')
    numB = int(input("Digite o segundo número inteiro: "))

if numA > numB:
    numMaior = numA
    numMenor = numB
else:
    numMaior = numB
    numMenor = numA

#Encontrando números primos

i = numMenor
somaprimos = 0
while i <= numMaior:
    if i > 1 :
        j = 2
        ehprimo = True
        while j <= (i // 2):
            if (i % j) == 0:
                ehprimo = False
                break
            j += 1
        if ehprimo:
            print(i, end=", ")
            somaprimos += i
    i += 1

print(f'\nOs números primos entre {numMenor} e {numMaior} foram todos listados acima!')
#print(f' Se os números primos entre eles forem somados, o resultado será {somaprimos}.')
print("\n===========================================================================================================")

#Pausa o programa para apresentar o resultado
print("Aperte ENTER para finalizar...")
input()  # Aguarda o usuário pressionar ENTER
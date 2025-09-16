#Lote 1.1
'''
LO01_ESTREP34
Receba um número. Calcule e mostre os resultados da tabuada desse número.


'''
print("Este programa recebe um número e mostra a tabuada deste número.")
print("===========================================================================================================")
# declarando variável e recebendo valores
numA = int(input("Digite um número: "))
i = 0
#mostrando a tabuada
while i <= 10:
    print(f"{numA} x {i} = {numA * i}")
    i += 1


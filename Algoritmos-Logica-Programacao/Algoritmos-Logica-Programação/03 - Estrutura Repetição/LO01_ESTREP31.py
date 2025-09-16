#Lote 1.1
'''
LO01_ESTREP31
Calcule e mostre o quadrado dos números entre 10 e 150.


'''
print("Este programa calcula e mostra os quadrados dos números entre 10 e 150.")
print("===========================================================================================================")
#declarando variavel e recebendo valores

for numberN in range(10, 151):
    quadrado = numberN * numberN
    print(f"O quadrado de {numberN} é: {quadrado}")
#fim_for
print("===========================================================================================================")
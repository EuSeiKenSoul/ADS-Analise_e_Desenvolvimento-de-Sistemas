# Lote 1.1
'''
LO01_ESTREP45
Calcule e mostre a série 1 – 2/4 + 3/9 – 4/16 + 5/25 + ... + 15/225
'''

print("Este programa calcula o valor da potência de um número.")
print("===========================================================================================================")
numerador=1
denominador=1
numeradorlimite=15
soma=0
i = numerador
while i <= numeradorlimite:
    if i % 2 == 0:
        soma = soma - (i / (denominador * denominador))
    else:
        soma = soma + (i / (denominador * denominador))
    numerador = numerador + 1
    denominador = denominador + 1
    i = i + 1
print("O resultado da série é: ", soma)
print("===========================================================================================================")
#pausa
input("Pressione <Enter> para encerrar...")

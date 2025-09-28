# Lote 1.1
'''
LO01_ESTREP42
Calcule e mostre a série 1 + 2/3 + 3/5 + ... + 50/99
'''

print("Este programa calcula e mostra a série 1 + 2/3 + 3/5 + ... + 50/99")
print("===========================================================================================================")
# declarando variável e recebendo valores e validando entrada de dados
numerador=1
denominador=1
numeradorlimite=50

soma=0
while numerador<=numeradorlimite:
    soma+=(numerador/denominador)
    numerador+=1
    denominador+=2
print("O resultado da série 1 + 2/3 + 3/5 + ... + 50/99 é: {:.2f}".format(soma))
print("===========================================================================================================")

#pausa
print("Pressione ENTER para sair")
input()

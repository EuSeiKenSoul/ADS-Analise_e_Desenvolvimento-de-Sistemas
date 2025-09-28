#Lote 1.1
'''
LO01_ESTDIC20
Receba 3 coeficientes A, B e C de uma equação do 2º grau da fórmula 
AX²+BX+C=0. Verifique e mostre a existência de raízes reais e se caso 
exista, calcule e mostre. 


'''
print("Este programa compara dois valores e mostra o maior deles.")
print("===========================================================================================================")

#declarando variavel e recebendo valores
numA = float(input("Digite um valor para A:  "))
while numA <=0 :
    print(f'Valor inválido, digite um valor maior que zero')
    numA = float(input("Digite um valor para A: "))

numB = float(input("Digite um valor para B:  "))
numC = float(input("Digite um valor para C:  "))


discriminante = 0
raiz_discriminante = 0
raiz_real = 0
raiz_real_negativa = 0

discriminante = (numB*numB)-(4*(numA*numC))
raiz_discriminante = discriminante ** 0.5
raiz_real = (-(numB)+(raiz_discriminante))/(2*numA)
raiz_real_negativa = (-(numB)-(raiz_discriminante))/(2*numA)
if discriminante > 0 :
    #duas reaizes reais distintas
    print(f'\nExitem duas raízes reais distintas e o resultado delas são:\n\n')
    print(f'Raíz positiva é {raiz_real}')
    print(f'Raíz negativa é {raiz_real_negativa}')
    
elif discriminante == 0:
    #uma raiz real e unica
    print(f'\nExite apenas uma raíz real única e o resultado dela é:\n\n')
    print(f'Raíz real única é {raiz_real}')

elif discriminante < 0:
    #não exitem raizes reais
    print(f'\nNão existem raizes reais com estes coeficientes.\n\n')

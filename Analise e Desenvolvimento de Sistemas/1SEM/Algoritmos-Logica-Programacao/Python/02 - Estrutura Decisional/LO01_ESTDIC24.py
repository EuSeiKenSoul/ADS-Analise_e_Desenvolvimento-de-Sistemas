#Lote 1.1
'''
LO01_ESTDIC24
Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3.  

'''
###################################################################################




        

print("Este programa verifica se um número é divisível por 2 e por 3.")
print("================================================================================================================================")
#declarando variavel
numUm = 0


#entrada de valores
numUm = int(input(f'Digite o primeiro número:  '))
while numUm <=0:
    print(f'Número não pode ser negativo!')
    numUm = int(input(f'Digite o primeiro número:  '))



#Resolução
if numUm % 2 == 0 or numUm % 3 == 0:
    #divisível pr 2 ou por 3
    if numUm % 2 == 0 and numUm % 3 != 0:
        #apenas divisível por 2
        print(f'Apenas divisível por 2')

    elif numUm % 3 == 0 and numUm % 2 != 0:
        #apenas divisível por 3
        print(f'Apenas divisível por 3')

    elif numUm % 2 == 0 and numUm % 3 == 0:
        #divisível por 2 e por 3
        print(f'Divisivel por 2 e por 3')
else:
    print(f'Número não é divisível por 2 ou 3')
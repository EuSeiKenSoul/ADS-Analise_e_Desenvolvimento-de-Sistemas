#Lote 1.1
'''
LO01_ESTDIC21
Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3. 

'''
###################################################################################



print("Este programa define a divisibilidade de um número por 2 e por 3.")
print("================================================================================================================================")
#declarando variavel e recebendo valores

num = int(input(f'Digite um número: '));




#Solucionando problema ou realizando calculos

if num % 2 == 0 and num % 3 == 0:
    print(f'O número {num} tem divisivilidade por 2 e por 3.');
elif num % 2 == 0:
    print(f'O número {num} tem divisibilidade apenas por 2');
elif num % 3 == 0:
    print(f'O número {num} tem divisibilidade apenas por 3');
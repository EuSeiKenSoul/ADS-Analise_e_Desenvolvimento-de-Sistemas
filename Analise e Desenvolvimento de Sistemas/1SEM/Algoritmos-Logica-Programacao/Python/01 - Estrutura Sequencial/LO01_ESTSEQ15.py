#Lote 1.1
'''
LO01_ESTDSEQ15
Receba os valores de 2 catetos de um triângulo retângulo. Calcule e mostre a hipotenusa. 
'''
###################################################################################



print(" Este programa calcula a hipotenusa de um triângulo retângulo, a partir do valor dos catetos. ");
print("================================================================================================================================");
catetoUm = float(input("Digite o valor do primeiro cateto: "));
catetoDois = float(input("Digite o valor do segundo cateto: "));
hipotenusa = ((catetoUm**2)+(catetoDois**2))**0.5;
print(f'O valor da hipotenusa é {hipotenusa}');
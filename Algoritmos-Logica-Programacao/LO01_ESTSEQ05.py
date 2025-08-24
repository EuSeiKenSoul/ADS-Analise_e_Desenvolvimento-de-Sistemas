#Lote 1.1
#LO01_ESTSEQ05
print("Este programa mostra as raízes reais considerando que a equação possue duas raízes")
print("==================================================================================")
#declarando variavel e recebendo valores
numA = float(input("Insira o número A: "));
numB = float(input("Insira o número B: "));
numC = float(input("Insira o número C: "));
#Solucionando problema ou calculos

delta = (numB*numB)*(-4*(numA*numC));

resPo = ((-numB+(delta**0.5))*(2*numA));
resNe = ((-numB-(delta**0.5))*(2*numA));

#apresentando resultados
print("==================================================================================")
print("A raiz real positiva é :",resPo);
print("A raiz real negativa é :",resNe);

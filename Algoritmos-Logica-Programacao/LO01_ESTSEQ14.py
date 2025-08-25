#Lote 1.1
#LO01_ESTSEQ10
# Receba 2 ângulos de um triângulo. Calcule e mostre o valor do 3º ângulo. 

print("Este programa calcula o terceiro ângulo de um triângulo.")
print("===========================================================================================================")
#declarando variavel e recebendo valores
anguloUm = float(input("Digite o angulo de uma das pontas de um triângulo: "));
anguloDois = float(input("Digite o angulo de uma das pontas de um triângulo: "));


#Solucionando problema ou realizando calculos
anguloTres = 180-(anguloUm+anguloDois);


print("====================================================")
print(" O terceiro ângulo do triângulo é ", anguloTres, " graus.");
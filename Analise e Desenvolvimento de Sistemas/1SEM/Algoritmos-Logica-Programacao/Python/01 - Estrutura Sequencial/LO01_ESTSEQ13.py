#Lote 1.1
#LO01_ESTSEQ10
# Receba o ano de nascimento e o ano atual. Calcule e mostre a sua idade e quantos anos terá daqui a 17 anos. 

print("Este programa calcula a duração de uma certa quantia de peso de alimentos para um consumo de 50g por dia.")
print("===========================================================================================================")
#declarando variavel e recebendo valores
alimentosQuilos = int(input("Digite a Quantidade de Quilos de alimento disponivéis: "));



#Solucionando problema ou realizando calculos
alimentosGramas = (alimentosQuilos*1000);
alimentoDuracao = (alimentosGramas/50);


print("====================================================")
print("Os ",alimentosQuilos," quilos podem durar ",alimentoDuracao, " dias.");
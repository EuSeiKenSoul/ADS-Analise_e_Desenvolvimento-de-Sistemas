#Lote 1.1
'''
LO01_MOD17
Calcule a quantidade de litros gastos em uma viagem, sabendo que o automóvel faz 12 km/l. Receber o tempo de percurso e a velocidade média. 
'''
###################################################################################
def calculo_gasto_combustivel():
    distancia = tempoPercurso * velocidadeMedia
    litrosGastos = distancia / 12
    print(f"A quantidade de litros gastos na viagem é de {litrosGastos:.2f} litros")


print("Este programa calcula a quantidade de litros gastos em uma viagem, sabendo que o automóvel faz 12 km/l.")
print("================================================================================================================================")
tempoPercurso = float(input("Digite o tempo de percurso em horas: "))
velocidadeMedia = float(input("Digite a velocidade média em km/h: "))
calculo_gasto_combustivel()
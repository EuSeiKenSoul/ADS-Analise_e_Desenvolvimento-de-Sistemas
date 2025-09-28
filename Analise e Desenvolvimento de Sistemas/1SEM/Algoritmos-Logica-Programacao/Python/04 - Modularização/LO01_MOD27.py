#Lote 1.1
'''
LO01_ESTDIC27
Receba o número de voltas, a extensão do circuito (em metros) e o tempo de duração (minutos). Calcule e mostre a velocidade média em km/h. 

'''
###################################################################################
#MODULOS
def calc_vel_media():  
    #Resolução do problema 
    distMetros = numVoltas*metrosCircuito
    distKm=distMetros/1000
    tempoDuracaoHoras = tempoDuracaoMin/60
    veloKMph = distKm/ tempoDuracaoHoras
    print(f' A velocidade média foi de {veloKMph} KM/h')


print("Este programa calcula a velocidade média de um carro de corrida.")
print("================================================================================================================================")
#declarando variaveis e recebendo valores/dados
numVoltas = int(input(f'Digite o número de voltas: '))
while numVoltas <=0 :
    print(f'A valor não pode ser menor ou igual a zero!\n')
    numVoltas = int(input(f'Digite o número de voltas: '))

metrosCircuito = int(input(f'Digite a extensão do circuito (em metros): '))
while metrosCircuito <= 0:
    print(f'A valor não pode ser menor ou igual a zero!\n')
    metrosCircuito = int(input(f'Digite a extensão do circuito (em metros): '))

tempoDuracaoMin = int(input(f'Digite o tempo de duração (minutos):  '))
while tempoDuracaoMin <= 0:
    print(f'A valor não pode ser menor ou igual a zero!\n')
    tempoDuracaoMin = int(input(f'Digite o tempo de duração (minutos):  '))

#Invocando modulo
calc_vel_media()
                            
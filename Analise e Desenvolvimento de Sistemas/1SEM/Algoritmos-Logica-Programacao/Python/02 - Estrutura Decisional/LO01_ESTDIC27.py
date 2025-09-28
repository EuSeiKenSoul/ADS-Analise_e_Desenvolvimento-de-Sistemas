#Lote 1.1
'''
LO01_ESTDIC27
Receba o número de voltas, a extensão do circuito (em metros) e o tempo de duração (minutos). Calcule e mostre a velocidade média em km/h. 

'''
###################################################################################



print("Este programa calcula a velocidade média de um carro de corrida.")
print("================================================================================================================================")
#declarando variavel e recebendo valores/dados
numVoltas = int(input(f'Digite o número de voltas: '));
metrosCircuito = int(input(f'Digite a extensão do circuito (em metros): '));
tempoDuracaoMin = int(input(f'Digite o tempo de duração (minutos):  '));

#Resolução do problema
#Tratando erro em caso de valor com zero ou negativo
if ( numVoltas <= 0 or metrosCircuito <= 0 or tempoDuracaoMin <= 0):
    print('Os valores não podem ser menor ou igual a zero')
else:
    distMetros = numVoltas*metrosCircuito;
    distKm=distMetros/1000;
    tempoDuracaoHoras = tempoDuracaoMin/60;
    veloKMph = distKm/ tempoDuracaoHoras;
    print(f' A velocidade média foi de {veloKMph} KM/h');
                            
#Lote 1.1
'''
LO01_ESTDIC26
Receba a hora de início e de final de um jogo (HH,MM), calcular o tempo do 
jogo em horas e minutos, sabendo que o tempo máximo é menor que 24 
horas e pode começar num dia e terminar noutro.  

'''
###################################################################################



print("Este programa calcula a duração de um jogo a partir do horario fornecido pelo usuário.")
print("================================================================================================================================")
#declarando variavel e recebendo valores/dados

print(f'Entre com o horario do inicio do jogo.')
horaIni = int(input(f'Digite a hora: '));
minutoIni = int(input(f'Digite a minuto: '));

print(f'Entre com o horario do final do jogo.')
horaFim = int(input(f'Digite a hora: '));
minutoFim = int(input(f'Digite a minuto: '));
horaJogo = 0;
minutoJogo = 0;


#Solucionando problema ou realizando calculos

if ( horaFim < horaIni):
    horaJogo = (24 - horaIni)+horaFim;
    if (minutoIni == minutoFim) :
        minutoJogo = 0;
        
    elif (minutoIni < minutoFim) :
        minutoJogo = minutoFim-minutoIni;
    else:
        minutoJogo = (60 - minutoIni)+minutoFim;
        
    #print(f'===========if true is {horaJogo} e {minutoJogo}'); Usei esse comando para verificar valores das variaveis em tempo de execução
else:
    horaJogo = horaFim-horaIni;
    minutoJogo = minutoFim-minutoIni;
    #print(f'===========if false is {horaJogo} e {minutoJogo}'); Usei esse comando para verificar valores das variaveis em tempo de execução


#arrumando minutos para não ser superior ou igual a 60
while minutoJogo >=60 :
    #print(f'===========While true is INI {horaJogo} e {minutoJogo}'); Usei esse comando para verificar valores das variaveis em tempo de execução
    horaJogo = horaJogo + 1;
    minutoJogo = minutoJogo -60;
    #print(f'===========While true is FIM {horaJogo} e {minutoJogo}'); Usei esse comando para verificar valores das variaveis em tempo de execução

# Apresentando resultados e soluções

print(f' O jogo durou {horaJogo} horas e {minutoJogo} minutos.')
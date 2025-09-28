# Lote 1.1
'''
LO01_ESTREP39
Calcule a quantidade de grãos contidos em um tabuleiro de xadrez onde: 
Casa:  1 2 3 4 ... 64 
Qdte: 1 2 4 8 ... N
'''

print("Este programa calcula a quantidade de grãos contidos em um tabuleiro de xadrez onde:")
print("===========================================================================================================")

# declarando variáveis
numCasas = 64  # fixo, mas pode ser alterado
numSementes = 1  # sementes na 1ª casa
totalSementes = 0  # acumulador

# processamento
i = 1
while i <= numCasas:
    totalSementes += numSementes
    print(f'Casa {i} - {numSementes} sementes, total acumulado: {totalSementes}')
    numSementes *= 2  # dobra a cada casa
    i += 1

print(f'\nTOTAL DE SEMENTES NO TABULEIRO: {totalSementes}\n')



#Pausa o programa para apresentar o resultado
print("Aperte ENTER para finalizar...")
input()  # Aguarda o usuário pressionar ENTER

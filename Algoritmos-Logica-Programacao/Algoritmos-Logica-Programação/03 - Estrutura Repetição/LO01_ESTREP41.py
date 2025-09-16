# Lote 1.1
'''
LO01_ESTREP41
Mostre todas as possibilidades de 2 dados de forma que a soma tenha como 
resultado 7. 
'''

print("Este programa mostra todas as possibilidades de 2 dados de forma que a soma tenha como resultado 7.")
print("===========================================================================================================")
# declarando variável e recebendo valores e validando entrada de dados
dadoslados=6
resultadosprocurado=7
i = 1
j = 1
print("As combinações possíveis são: ")
while i <= dadoslados:
    j = 1
    while j <= dadoslados:
        if i + j == resultadosprocurado:
            print(f'({i},{j}) ', end=' ')
        j += 1
    i += 1
    
# mostrando o resultado
print(f'')

print("===========================================================================================================")
#Pausa o programa para apresentar o resultado
print("Aperte ENTER para finalizar...")
input()  # Aguarda o usuário pressionar ENTER


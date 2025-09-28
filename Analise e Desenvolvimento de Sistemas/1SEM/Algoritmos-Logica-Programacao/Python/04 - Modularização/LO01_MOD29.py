#Lote 1.1
'''
LO01_ESTRDIC29
Receba o tipo de investimento (1 = poupança e 2 = renda fixa) e o valor do investimento. Calcule e mostre o valor corrigido em 30 dias sabendo que a poupança = 3% e a renda fixa = 5%. Demais tipos não serão considerados. 
'''
###################################################################################
#MODULOS
def calc_invesstimento():
    if (opSelection == 1):
        valorRendimento = 1.03
        valorCorrigido = valorInvestido * valorRendimento
        print(f'O valor corrigido do investimento em poupança é R$ {valorCorrigido:.2f}')
    elif (opSelection == 2):
        valorRendimento = 1.05
        valorCorrigido = valorInvestido * valorRendimento
        print(f'O valor corrigido do investimento em renda fixa é R$ {valorCorrigido:.2f}')
    else:
        print("Tipo de investimento inválido!")


print("Este programa calcula o valor corrigido de um investimento em 30 dias.")
print("================================================================================================================================")
opSelection = int(input("Digite 1 para poupança ou 2 para renda fixa: "))
while opSelection < 1 or opSelection > 2:
    print(f'Opção inválida!')
    opSelection = int(input("Digite 1 para poupança ou 2 para renda fixa: "))

valorInvestido = float(input("Digite o valor do investimento: R$ "))
while valorInvestido <= 0:
    print(f'Valor de investimento deve ser maior que zero!')
    valorInvestido = float(input("Digite o valor do investimento: R$ "))

#invocar modulo
calc_invesstimento()

#Lote 1.2
'''
LO01_MOD16
Receba a quantidade de horas trabalhadas, o valor por hora, o percentual de desconto e o número de dependentes.
Calcule o salário que serão as horas trabalhadas x o valor por hora. Calcule o salário líquido (= Salário bruto – desconto).
A cada dependente será acrescido R$ 100 no Salário Líquido. Exiba o salário a receber. 
'''
###################################################################################
def Calculo_Salario_a_Receber():
    salarioBruto = horasTrabalhadas * valorPorHora;
    desconto = (salarioBruto * percentualDesconto) / 100;
    salarioLiquido = (salarioBruto - desconto)+ (numeroDependentes * 100);
    print(f'O Salário a receber é R${salarioLiquido}');

print(" Este programa calcula o salário a receber.")
print("================================================================================================================================")
horasTrabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
valorPorHora = float(input("Digite o valor por hora trabalhada: "))
percentualDesconto = float(input("Digite o percentual de desconto: "))
numeroDependentes = int(input("Digite o número de dependentes: "))





Calculo_Salario_a_Receber()
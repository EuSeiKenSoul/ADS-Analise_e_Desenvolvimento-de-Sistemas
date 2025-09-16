#Lote 1.1
#LO01_ESTSEQ10
# Receba o ano de nascimento e o ano atual. Calcule e mostre a sua idade e quantos anos terá daqui a 17 anos. 

print("Este programa calcula a idade atual com base nos anos fornecidos pelo usuário")
print("================================================================================")
#declarando variavel e recebendo valores
anoNasc = int(input("Digite o ano de nascimento: "));
anoAtual = int(input("Digite o ano atual: "));


#Solucionando problema ou realizando calculos
idadeAtual=(anoAtual-anoNasc);
idadeFutura = (idadeAtual+17);


print("====================================================")
print("Com base nos anos fornecidos e idade atual é ",idadeAtual," anos e daqui 17 anos o sujeito tera ", idadeFutura, "anos.");
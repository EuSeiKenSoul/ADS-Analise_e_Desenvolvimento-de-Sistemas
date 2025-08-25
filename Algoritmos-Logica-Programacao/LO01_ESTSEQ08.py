#Lote 1.1
#LO01_ESTSEQ08
#Receba  o  valor  de  um  depósito  em  poupança.  Calcule  e  mostre  o  valor após 1 mês de aplicação sabendo que rende 1,3% a. m.

print("Este programa calcula o rendimento de um deposito em poupança rendendo 1,3% a.m.")
print("================================================================================")
#declarando variavel e recebendo valores
valorPoup = int(input("Digite um valor para ser Depositado: "));

#Solucionando problema ou realizando calculos

valorComRend = (valorPoup+(valorPoup*0.013));


print("====================================================")
print("Seus " ,valorPoup,"R$ rendeu ",valorPoup*0.013,"R$ no ultimo mês e você tem no momento ",valorComRend,"R$");


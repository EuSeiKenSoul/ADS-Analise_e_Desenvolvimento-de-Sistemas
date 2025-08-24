#Lote 1.1
#LO01_ESTSEQ06
print("Este programa troca os valores entre duas variáveis.")
print("====================================================")
#declarando variavel e recebendo valores
numX = int(input("Digite um valor para ser colocado na Caixa A: "));
numY = int(input("Digite um valor para ser colocado na Caixa B: "));
#Solucionando problema ou realizando calculos

temp = numX;
numX = numY;
numY = temp;



print("O número dentro da caixa A agora é :",numX);
print("O número dentro da caixa B agora é :",numY);

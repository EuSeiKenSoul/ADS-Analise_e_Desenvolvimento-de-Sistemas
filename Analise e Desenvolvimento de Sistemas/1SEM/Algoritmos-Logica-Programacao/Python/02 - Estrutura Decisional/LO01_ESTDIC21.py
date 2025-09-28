#Lote 1.1
'''
LO01_ESTDIC21
Receba 4 notas bimestrais de um aluno. Calcule e mostre a média aritmética. 
Mostre a mensagem de acordo com a média: 
a. Se a média for >= 6,0 exibir “APROVADO”; 
b. Se a média for >= 3,0 E < 6,0 exibir “EXAME”; 
c. Se a média for < 3,0 exibir “RETIDO”.


'''
###################################################################################



print("Este programa calcule média aritmética entre quatro notas e informa se aluno foi aprovado, se deve fazer exame ou se foi retido.")
print("================================================================================================================================")
#declarando variavel e recebendo valores
notaUm = float(input("Digite a primeira nota:  "));
notaDois = float(input("Digite a segunda nota:  "));
notaTres = float(input("Digite a terceira nota:  "));
notaQuatro = float(input("Digite a quarta nota:  "));



#Solucionando problema ou realizando calculos
media = ((notaUm+notaDois+notaTres+notaQuatro)/4);
if (media >=6) :
    
    print("====================================================");
    print (f' A Média é {media} portanto o aluno está APROVADO!');
elif (media >=3 and media <6):
    print("====================================================");
    print (f' A Média é {media} portanto o aluno precisa fazer EXAME!');
elif (media <3):
    print("====================================================");
    print (f' A Média é {media} portanto o aluno foi RETIDO!');


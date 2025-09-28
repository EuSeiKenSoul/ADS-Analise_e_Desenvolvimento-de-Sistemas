# Lote 1.1
'''
LO01_ESTREP43
Calcule e mostre quantos anos serão necessários para que Ana seja maior que 
Maria sabendo que Ana tem 1,10 m e cresce 3 cm ao ano e Maria tem 1,5 m 
e cresce 2 cm ao ano.
'''

print("Este programa calcula quantos anos serão necessários para que Ana seja maior que Maria.")
print("===========================================================================================================")
anoatual = 0
altura_ana = 1.10
altura_maria = 1.50
taxa_crescimento_ana = 0.03
taxa_crescimento_maria = 0.02
while altura_ana <= altura_maria:
    anoatual += 1
    altura_ana += taxa_crescimento_ana
    altura_maria += taxa_crescimento_maria
print(f"Serão necessários {anoatual} anos para que Ana seja maior que Maria.")
print("===========================================================================================================")
#pausa
input("Pressione <Enter> para encerrar...")

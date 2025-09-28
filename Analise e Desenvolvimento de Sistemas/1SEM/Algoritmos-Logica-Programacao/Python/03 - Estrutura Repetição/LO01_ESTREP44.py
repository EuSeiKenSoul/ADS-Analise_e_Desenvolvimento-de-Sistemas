# Lote 1.1
'''
LO01_ESTREP44
Receba o número da base e do expoente. Calcule e mostre o valor da 
potência. 
'''

print("Este programa calcula o valor da potência de um número.")
print("===========================================================================================================")
base = int(input("Digite o número da base: "))
while base <= 0:
    print("Número inválido! A base deve ser um número inteiro positivo.")
    base = int(input("Digite o número da base: "))
expoente = int(input("Digite o número do expoente: "))
while expoente < 0:
    print("Número inválido! O expoente deve ser um número inteiro não negativo.")
    expoente = int(input("Digite o número do expoente: "))

potencia = base ** expoente
print(f"O valor da potência de {base} elevado a {expoente} é: {potencia}.")
print("===========================================================================================================")
#pausa
input("Pressione <Enter> para encerrar...")
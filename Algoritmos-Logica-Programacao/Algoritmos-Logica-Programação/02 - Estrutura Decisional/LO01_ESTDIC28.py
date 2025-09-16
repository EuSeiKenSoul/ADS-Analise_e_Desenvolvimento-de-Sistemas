#Lote 1.1
'''
LO01_ESTDIC28
Receba o preço atual e a media mensal de um produto. Calcule e mostre o novo preço, sabendo que:

'''
###################################################################################



print("Este programa calcula o novo preço de um produto baseado no preço atual e na média mensal.");
print("================================================================================================================================");

precoAtual = float(input("Digite o preço atual do produto: "));
mediaProduto = float(input("Digite a média mensal do produto: "));
if (mediaProduto < 500 and precoAtual < 30):
    novoPreco = precoAtual * 1.10;
    print(f'o Produto deve receber um aumento de 10% e ter seu preço atualizado para {novoPreco}R$');
elif (mediaProduto >= 500 and mediaProduto <= 1000 and precoAtual >= 30 and precoAtual <= 80):
    novoPreco = precoAtual * 1.15;
    print(f'o Produto deve receber um aumento de 15% e ter seu preço atualizado para {novoPreco}R$');
elif (mediaProduto > 1000 and precoAtual > 80):
    novoPreco = precoAtual * 0.95;
    print(f'o Produto deve receber um desconto de 5% e ter seu preço atualizado para {novoPreco}R$');
else:
    novoPreco = precoAtual;
    print(f'o Produto não deve receber nenhum reajuste e deve manter seu preço em {novoPreco}R$');
    
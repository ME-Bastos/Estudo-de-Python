#Pergunta a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
print('-'*20)
print('ALUGUEL DE CARROS!')
print('-'*20)
km=float(input('Quantos kilometros foram percorridos com o carro que você alugou? '))
dias=int(input('E por quantos dias foi alugado? '))
kmp= km * 0.15
diasp= dias * 60
valor= kmp + diasp
print('-'*20)
print(f'O valor final do aluguel fica R${valor:.2f}')
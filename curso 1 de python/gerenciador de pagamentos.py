#Calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto; à vista no cartão: 5% de desconto; em até 2x no cartão: preço normal 
# 3x ou mais no cartão: 20% de juros
print('CALCULO DE PAGAMENTOS: ')
pro=float(input('Digite o valor do produto: '))
r=int(input('Forma de pagamento: \n'
'Digite (1) se for à vista com dinheiro/cheque \n' \
'Digite (2) se for à vista no cartão \n' \
'Digite (3) se for em até 2 vezes no cartão \n' \
'Digite (4) se for em 3 vezes ou mais no cartão: \n'))
if r == 1:
    dsc= pro*10/100
    pf= pro-dsc
    print (f'O preço final do produto é {pf:.2f}')
elif r == 2:
    dsc = pro*5/100
    pf = pro-dsc
    print(f'O preço final do produto é {pf:.2f}')
elif r == 3:
    print(f'O preço final do produto é {pro:.2f}')
else:
    juro = pro*20/100
    pf = pro+juro
    print(f'O preço final do produto é {pf:.2f}')
#pedir para digitar a quantidade de dinheiro que tem na carteira
#converter para dolar e aparecer a quantidade de dolar que tem
#também converter para euro 
dinheiro=float(input('Quantos reais você tem? R$'))
dolar = dinheiro / 5.16 #preço do dolar atual (06.04.2026)
euro = dinheiro / 5.96 #preço do euro atual
print (f'Você conseguiria comprar {dolar:.2f} dolares ou {euro:.2f} euros')
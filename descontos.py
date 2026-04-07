#mostra o preço do produto e depois o preço com desconto de 5%
import os
import time
preço=float(input('Digite o preço do produto: R$'))
desconto= preço*5/100
preçofinal= preço-desconto
print (f'O preço do produto com 5% de desconto fica: R${preçofinal}') #ate aonde vai a aula

time.sleep(2)  # pausa por 2 segundos para ver o resultado
os.system('cls') #limpa a tela
preço=float(input('Digite o preço inicial do produto: R$'))
desconto=float(input('Digite o desconto do produto:'))
desconto1= preço*desconto/100
preçofinal=preço-desconto1
print(f'O preço do produto final com o desconto de {desconto}% fica {preçofinal}')
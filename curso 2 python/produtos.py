#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. 
#A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
total = p1000 = b = 0
while True:
    nome=input('Digite o nome do produto: ')
    p=float(input('Digite o preço do produto: '))
    r=input('Você quer continuar? [S/N] ').strip().upper()
    print ('---------------------------------------------')
    total += p
    if p >= 1000:
        p1000 +=1
    if b == 0 or p < b:
        b = p
        nb = nome
    if r == 'N':
        break
print(f'O total gasto foi {total}, houveram {p1000} produtos maiores que 1000 reais e o produto mais barato foi o {nb}')
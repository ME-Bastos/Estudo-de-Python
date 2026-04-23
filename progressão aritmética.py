#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
print('PROGRESSÃO ARITMÉTICA')
n=int(input('Digite o primeiro termo: '))
r=int(input('Digite a razão: '))
dec=n+(10-1) * r
for c in range (n, dec, r):
    print (f'{c}')

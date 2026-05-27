#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
print('PROGRESSÃO ARITMÉTICA')
n=int(input('Digite o primeiro termo: '))
r=int(input('Digite a razão: '))
termo=n
cont=1
total=0
mais=10
while mais != 0:
    total= total + mais
    while cont<=total:
        print(f'{termo} → ', end='')
        termo+=r
        cont+=1
    print('PAUSA')
    mais=int(input('Quantos termos ainda quer mostrar? '))
print(f'Progressão finalizada com {total} números mostrados')
#dec=n+(10-1) * r
#for c in range (n, dec, r):
#    print (f'{c}')

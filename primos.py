#leia um número inteiro e diga se ele é ou não um número primo.
n=int(input('Digite um número: '))
tot = 0
for c in range (1, n+1):
    if n % c == 0:
        tot += 1
print(f'O número {n} foi divisivel {tot} vezes')
if tot == 2:
    print('O número é primo.')
else:
    print('O número não é primo.')
#leia um número qualquer e mostre o seu fatorial.
from math import factorial
n=int(input('Digite um número para calcular o seu fatorial: '))
f=(factorial(n))
c=n
while c > 0:
    print(f'{n} x ', end='')
    c-=1
    n-=1
print(f'O fatorial é igual a {f}')
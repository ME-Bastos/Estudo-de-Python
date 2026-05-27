#gerar cinco números aleatórios e colocar em uma tupla. 
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
n = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print (f'Foram gerados os números: {n}')
print(f'O maior valor da tupla foi {max(n)} e o menor foi {min(n)}')
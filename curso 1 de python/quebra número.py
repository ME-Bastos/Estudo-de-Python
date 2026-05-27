#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math #importa mais contas matematicas
Num=float(input('Digite um número:'))
inn= math.trunc(Num) #simplesmente apaga o que tem depois da virgula
print(f'O número {Num} tem a parte inteira de {inn}')
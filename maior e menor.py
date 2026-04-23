#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior=0
menor=0
for c in range (1, 6):
    peso=float(input(f'Digite o peso da {c} pessoa: '))
    if c == 1:
        menor=peso
        maior=peso
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(f'O maior peso foi de {maior}kg e o menor foi de {menor}kg')

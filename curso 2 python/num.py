#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#  O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores
r = 's'
soma = cont = 0
while r != 'N':
    n=int(input('Digite um número inteiro: '))
    soma += n
    cont +=1
    if cont == 1: 
        maior = menor = n
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    r=str(input('Você quer continuar? [s/n]: ')).upper()
m = soma / cont
print(f'Acabou a execução!\nA soma dos valores digitados é: {soma}\nA média entre os valores digitados é: {m}\nO maior valor digitado é: {maior}\nEnquanto o menor é: {menor}')
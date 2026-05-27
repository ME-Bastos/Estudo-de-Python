# Crie um programa que leia dois valores e mostre um menu na tela:[ 1 ] somar;[ 2 ] multiplicar;[ 3 ] maior;[ 4 ] novos números; [ 5 ] sair do programa
import os
import time
r=1
print('CALCULADORA! ')
while r != 5: #enquanto diferente de 5
    n1=int(input('Digite um número: '))
    n2=int(input('Digite outro: '))
    print('O que você quer fazer?')
    r=int(input('''Digite:
                 [1] se quiser somar
                 [2] se quiser multiplicar
                 [3] se quiser verificar o maior número 
                 [4] dividir os valores 
                 [5] sair do programa
                 Resposta: '''))
    if r==1:
        soma=n1+n2
        print(f'A soma dos dois valores é igual a: {soma}')
        time.sleep(2)  # pausa por 2 segundos para ver o resultado
        os.system('cls') #limpa a tela
    elif r==2:
        m=n1*n2
        print(f'A multiplicação dos dois valores é igual a: {m}')
        time.sleep(2)
        os.system('cls')
    elif r==3:
        if n1 > n2:
            print(f'O maior número é: {n1}')
        else:
            print(f'O maior número é: {n2}')
        time.sleep(2)
        os.system('cls')
    elif r==4:
        div=n1/n2
        print(f'A divisão dos dois valores é igual a: {div}')
        time.sleep(2)
        os.system('cls')
    else:
        print('Fim do programa.')
        
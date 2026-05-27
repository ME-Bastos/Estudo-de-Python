#funcionamento de um caixa eletrônico.
#Pergunte ao usuário qual será o valor a ser sacado e o programa vai informar quantas cédulas de cada valor serão entregues.
#caixa possui cédulas de R$50, R$20, R$10 e R$1.
valor=int(input('Digite o valor a ser sacado (só aceitamos valores inteiros): R$'))
total = valor
ced = 50
totced = 0

while True:
    if total >=ced:
        total -=ced
        totced +=1
    else:
        if totced > 0:
            print(f'Total de cédulas de {ced}: {totced}')
        totced = 0
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        if total == 0:
            break


n=int(input('Quantos números da sequência de fibonacci deseja colocar? '))
t1 , t2 = 0 , 1
print(f'{t1} → {t2}', end='')
t3=t1+t2
cont=3
while cont <= n:
    t3=t1+t2
    print(f' → {t3}', end='')
    cont+=1
    t1=t2
    t2=t3
print('\nFim da sequência.')

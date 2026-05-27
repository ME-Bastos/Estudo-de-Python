num=int(input('Digite um número para ver sua tabuada:'))
contador = 1

while contador <= 10: #limita o contador
    print(f'{num} x {contador} = {num*contador}')
    contador += 1 # aumenta o valor do contador
print ('Final do programa!')


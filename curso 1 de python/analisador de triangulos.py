#  Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('\033[1;34mAnalisador de triangulos!\033[0m') # jeito de botar cor no terminal python atualizado!
l1=float(input('Digite o valor do primeiro segmento: '))
l2=float(input('Digite o valor do segundo segmento: '))
l3=float(input('Digite o valor do terceiro segmento: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2: # se for um triangulo
    print ('Os segmentos acima podem formar um triangulo!')
    if l1 == l2 == l3:
        print ('O triangulo é equilátero')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print ('O triangulo é isósceles')
    else:
        print ('O triangulo é escaleno')
else: #else do primeiro if
    print ('Os segmentos acima não podem formar um triangulo.')

#– EQUILÁTERO: todos os lados iguais ISÓSCELES: dois lados iguais, um diferente ESCALENO: todos os lados diferentes


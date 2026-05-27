#leia um número inteiro
#peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
n=int(input('Digite um número inteiro: '))
r=int(input('Se você quiser converter para binário aperte [1], para octal aperte [2] e para hexadecimal aperte [3]: '))
if r == 1:
    print(f'{n} convertido para binário é igual a {bin(n)[2:]}')
elif r == 2:
    print (f'{n} convertido para octal é igual a {oct(n)[2:]}')
elif r == 3:
    print (f'{n} convertido para hexadecial é igual a {hex(n)[2:]}')
else:
    print ('Opção inválida! Tente novamente.')
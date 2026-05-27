import math

a=int(input('Digite um número:'))
print ('O tipo é ', type(a)) #Mostra que é inteiro
ant= a-1 #mostra o numero anterior
su= a+1 #mostra o próximo numero
print('O antecessor de {} é {} e o sucessor é {}'.format(a,ant,su))
print('='*20)
#dobro, triplo e raiz quadrada
d= a*2
tri=a*3
raiz= math.sqrt(a)
print('O dobro do valor digitado é {}, o triplo é {} e a raiz é {:.3}'.format(d,tri,raiz))
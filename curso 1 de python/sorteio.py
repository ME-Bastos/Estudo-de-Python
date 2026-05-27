# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
#lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import os #pra apagar a tela
import time #tempo
import random #repositório de aleatorio
n1=str(input('Digite o nome do 1. aluno: '))
n2=str(input('Digite o nome do 2. aluno: '))
n3=str(input('Digite o nome do 3. aluno: '))
n4=str(input('Digite o nome do 4. aluno: '))
lista = [n1,n2,n3,n4] #limita as escolhas para os nomes
escolhido = random.choice(lista) #decide qual vai ser o escolhido aleatoriamente
print (f'O(a) escolhido(a) foi {escolhido}!')

time.sleep(2)  # pausa por 2 segundos para ver o resultado
os.system('cls') #limpa a tela

#sortear a ordem de apresentação de trabalhos dos alunos. leia o nome dos quatro alunos e mostre a ordem sorteada.
n1=str(input('Digite o nome do 1. aluno: '))
n2=str(input('Digite o nome do 2. aluno: '))
n3=str(input('Digite o nome do 3. aluno: '))
n4=str(input('Digite o nome do 4. aluno: '))
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print ('A ordem das apresentações vai ser: ')
print(lista)
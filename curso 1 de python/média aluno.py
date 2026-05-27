#programa que lê as duas notas de um aluno e calcula a média
nome=str(input('Digite o nome do aluno:'))
n1=int(input('Digite sua primeira nota:'))
n2=int(input('Digite sua segunda nota:'))
m=(n1+n2)/2
print(f'A média do aluno é: {m}')
#f serve como o .format do final, porém menor
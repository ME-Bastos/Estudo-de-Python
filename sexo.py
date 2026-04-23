#leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo=''
while sexo == '':
    sexo=str(input('Digite o sexo [M/F]: '))
    if sexo not in 'MmFf':
        sexo == ''
        print('ERRO! TENTE NOVAMENTE.')
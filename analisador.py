#leia o nome, idade e sexo de 4 pessoas.
#mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
nomev=''
velho = 0
jovem = 0
media = 0
for c in range (1, 5):
    nome=str(input(f'Digite o nome da {c} pessoa: '))
    idade=int(input(f'Digite a idade da {c} pessoa: '))
    sexo=str(input(f'Digite o sexo da {c} pessoa (masc/fem):'))
    print('----------------------------------------------------------')
    media += idade
    if sexo == 'masc' and idade > velho:
        velho = idade
        nomev = nome
    elif sexo == 'fem' and idade < 20:
        jovem +=1
media = media/5
print(f'Entre os nomes digitados, o homem mais velho é o {nomev}, tem {jovem} mulheres mais novas do que 20 anos e a média das idades é {media}')
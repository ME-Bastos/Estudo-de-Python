a=input('Digite algo: ')
print('O tipo é ',type(a)) #mostra o tipo do que foi digitado
print('Só tem espaços?', a.isspace()) #mostra se só tem espaços
print('É um número?', a.isnumeric()) #se tem número
print('Só tem letras?', a.isalpha()) #se só tem letras
print('É alfanúmerico?', a.isalnum()) #se tem letras e/ou números
print('Tá tudo maiusculo?', a.isupper()) #se tá tudo no caps lock
print('Tá tudo minúsculo?', a.islower()) #se tá tudo com letra minúscula

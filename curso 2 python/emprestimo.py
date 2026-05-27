#Aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
print('Emprestimo!')
casa=float(input('Digite o valor da casa: '))
salario=float(input('Digite o seu salário atual: '))
anos=int(input('Digite em quantos anos você vai pagar: '))
sf= salario * 0.30
pm= casa / (anos * 12) 

if pm >= sf:
    print('O emprestimo não pode ser realizado.')
else:
    print('O emprestimo foi liberado.')
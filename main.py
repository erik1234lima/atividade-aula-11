a = float(input('Calcule o valor do salario: ').replace(',','.'))

b = float(input('Calcule o valor do aumento: ').replace(',','.'))

c = a * (b/100)
d = a+c
print('O valor do salario vai ser de R$%.2f'%d)

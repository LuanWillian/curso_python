salario = float(input('Digite seu salario em R$: '))
if salario <= 1250:
    novo = salario + (salario * 15/100)
    
else:
    novo = salario + (salario * 10/100)
    print('Seu salario foi de {} para {:.2f} Parabens!'.format(salario, novo))
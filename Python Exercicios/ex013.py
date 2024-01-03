salario = float(input('Qual e o salario do fucionario? '))
novo = salario + (salario * 15/100)
print('O funcionario que ganhava R${}, com 15% de almento, passa a ganhar R${:.2f}'.format(salario, novo))
 
km = int(input('Digite quantos km voce rodou: '))
d = float(input('Digete quantos dia voce ficou com carro: '))
a = (km * 0.15) + (d * 60)
print('O valor total a pagar e {:.2f}'.format(a))
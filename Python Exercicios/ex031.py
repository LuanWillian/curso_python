distancia = float(input('Digite a distancia da sua viagem: '))

if distancia <= 200:
    preco = distancia * 0.50

else:
     preco = distancia * 0.45

print('A distacia que voce ira e de {}km e o valor a ser pago e R${:.2f}'.format(distancia, preco))
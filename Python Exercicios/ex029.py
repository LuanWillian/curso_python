num = float(input('Digite a velocidade do carro: '))

if num > 80:
    multa = (num - 80) * 7
    print('MULTADO!! Voce passou do limite! O valor da multa e {:.2f}'.format(multa))

print('Dirija com cuidado! Tenha um otimo dia!')
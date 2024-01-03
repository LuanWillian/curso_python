peso = float(input('Qual seu peso?: '))
altura = float(input('Qual sua altura?: '))
imc = peso / (altura ** 2)
print('O imc da pessoa e {:.1f}'.format(imc))

if imc <= 18.5:
    print('Voce estar abaixo do peso!')

elif imc <= 25:
    print('Seu peso e normal!')

elif imc <= 30:
    print('Voce estar com sobrepeso!')

elif imc <= 40:
    print('Voce estar com obesidade!')

elif imc > 40:
    print('Voce estar com obesidade morbida!')
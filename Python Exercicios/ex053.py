frase = str(input('Digute uma frase: ')).strip().upper()
separa = frase.split()
juntar = ''.join(separa)
inverte = juntar[::-1]
print('A frase "{}" ao inverso e "{}"'.format(frase, inverte))

if juntar == inverte:
    print('Essa frase e POLINDROMO!')

else:
    print('Essa frase não e POLINDROMO!')
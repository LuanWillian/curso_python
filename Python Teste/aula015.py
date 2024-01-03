soma = 0
while True:
    numero = int(input('Numero: '))
    if numero == 999:
        break
    soma = soma + numero
#print('A soma vale {}'.format(soma))
print(f'A soma vale {soma}')
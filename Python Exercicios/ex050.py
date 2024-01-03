soma = 0
contador = 0
for c in range(1,7):
    number = int(input('Digite um numero: '))
    if number % 2 == 0:
        soma = soma + number
        contador = contador + 1
print('Os numeros pares que apareceu foi {} vezes a somas dos numeros foi {}'.format(contador,soma))

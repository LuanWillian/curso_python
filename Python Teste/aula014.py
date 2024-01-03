n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um numero: '))
    if n != 0:
        if n % 2 == 0:
            par = par +1
        else:
            impar = impar +1
print('Você digitou {} numeros pares e {} numeros impares!'.format(par, impar))
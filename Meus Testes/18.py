numero = int(input('Digite um numero para saber a sequencia de Fibonacci: '))
num1 = 0
num2 = 1
print('{} -> {}'.format(num1,num2),end='')
contador = 2
while not contador == numero:
    contador = contador +1
    num3 = num1 + num2
    print(' -> {}'.format(num3),end='')
    num1 = num2
    num2 = num3
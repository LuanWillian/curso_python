numero = int(input('Digite um numero para saber a sequencia de Fibonacci: '))
n1 = 0
n2 = 1
print('{} -> {}'.format(n1,n2),end='')
contador = 2
while contador < numero:
    contador = contador +1
    n3 = n1 + n2
    print(' -> {}'.format(n3),end='')
    n1 = n2
    n2 = n3
print(end=' ''Fim')
print(contador,numero)
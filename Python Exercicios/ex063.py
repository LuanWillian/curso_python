num = int(input('Digite um numero para saber a sequencia de fibonacci: '))
n1 = 0
n2 = 1
cont = 2
print('{} -> {}'.format(n1,n2),end='')
while cont < num:
    cont = cont+1
    n3 = n1 + n2
    print(' -> {}'.format(n3),end='')
    n1 = n2
    n2 = n3
print(end=' ''Fim')

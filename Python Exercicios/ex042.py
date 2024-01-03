
n1 = int(input('Digite o tamanho da reta: '))
n2 = int(input('Digite o tamanho da reta: '))
n3 = int(input('Digite p tamanho da reta: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos acima PODEM FORMA um triangulo ', end=(''))
    if n1 == n2 == n3:
        print('EQUILATERO!')
    elif n1 != n2 != n3 != n1:
        print('ESCALENO!')
    else:
        print('ISOSCELES!')

else:
    print('Os segmentos acima NÃO PODEM FORMAR um triangulo!')
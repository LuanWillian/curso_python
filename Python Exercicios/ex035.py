segmento1 = float(input('Digite o primeiro segmento: '))
segmento2 = float(input('Digite o segundo segmento: '))
segmento3 = float(input('Digite o terceiro segmento: '))

if segmento1 < segmento2 + segmento3 and segmento2 < segmento1 + segmento3 and segmento3 < segmento1 + segmento2:
    print('Forma um triangulo!')

else:
    print('Nao forma um triangulo')

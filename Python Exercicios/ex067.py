while True:
    numero = int(input('Quer ver a tabuada de qual valor?: '))
    if numero < 0:
        print('PROGRAMA TABUADA INCERADA! Volte sempre!')
        break
    for c in range(1,11):
        tabuada = c * numero
        print(f'{c} x {numero} = {tabuada}')
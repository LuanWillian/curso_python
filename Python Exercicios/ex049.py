number = int(input('Digite um numero para saber a sua tabuada: '))
for c in range(1,11):
    res = number * c
    print('{} x {} = {}'.format(number,c, res))
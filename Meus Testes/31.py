lista = [5, 4, 3, 2, 1]
mult = 1
for c in lista:
    mult *= c
    print(f'{c} x ', end='')
    if c == 2:
        print(f'1 = {mult}', end='')
        break
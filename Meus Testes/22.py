nomes = 'Luan'.upper(),'Luana'.upper(),'Paula'.upper(),'Jose'.upper(),'Maria'.upper()
for c in nomes:
    print('')
    print(f'\nO nome {c} Teve as segintes vogais:',end=' ')
    for i in c:
        if i in 'AEIOU':
            print(i,end='')

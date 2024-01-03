palavras = ('Carro','programar','Curso','Notbook','Python','Ventilador','Caixa')
for c in palavras:
    print('-' * 40)
    print(f'As palavras {c} teve as sequites vogais: ')
    for d in c:
        if d.upper() in 'AEIOU':
            print(f'{d}')
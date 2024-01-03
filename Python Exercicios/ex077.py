palavra = ('Carro','Programar','Aprender','Lua','Mouse','Roupa','Carregador',
           'Musica','Jazz','Bola','gato','Bolsa','Curso','Python','Fone')
for p in palavra:
    print(f'\nNa palavra {p.upper()} temos: ',end='')
    for letra in p:
        if letra.upper() == 'AEIOU':
            print(letra,end='')
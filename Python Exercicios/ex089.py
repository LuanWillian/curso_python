lista = []
opçao = 0
while True:
    nome = (str(input('Nome: ')))
    nota1 = (float(input('Nota 1: ')))
    nota2 = (float(input('Nota 2: ')))
    media = nota1 + nota2 / 2
    lista.append([nome, [nota1, nota2], media])
    usuario = str(input('Quer continuar? [S/N]: ')).upper()[0]
    if usuario == 'N':
        print('=-'*20)
        print(f'{"N.":<4} {"NOME":<10} {"MEDIA":>8}')
        print('-'*30)
        for n, c in enumerate(lista):
            print(f'{n:<4} {c[0]:<10} {c[2]:>8}')
        while opçao != 999:
            print('-'*80)
            opçao = int(input(f'Mostrar notas de qual aluno? (999 para interromper): '))
            if opçao <= len(lista)-1:
                print(f'Notas de {lista[opçao][0]} são: {lista[opçao][1]}')
        break
contidade = 0
contM = 0
contF = 0
while True:
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'FM':
        sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
    idade = int(input('Digite sua idade: '))
    usuario = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while usuario not in 'SN':
        usuario = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

    if idade > 18:
        contidade = contidade +1
    if sexo == 'M':
        contM = contM +1
    if sexo == 'F' and idade < 20:
        contF = contF +1
    
    if usuario == 'N':
        print(f'Total de pessoas com mais de 18 anos: {contidade}')
        print(f'Ao todo temos {contM} homens cadastrado')
        print(f'E tomos {contF} mulheres com menos de 20 anos')
        break
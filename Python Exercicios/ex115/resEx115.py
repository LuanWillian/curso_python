import defs
usuario = 0
while True:
    print('-'*40)
    print('           MENU PRINCIPAL')
    print('-'*40)
    print('1 - Ver pessoas cadastradas\n2 - Cadastra nova pessoa\n3 - Sair do sistema')
    print('-'*40)

    try:
        usuario = int(input('Sua opção: '))
        if usuario > 3 or usuario == 0:
            print('ERRO! Digite uma opção valida!')

    except ValueError:
        print('ERRO! Digite uma opção valida!')
        if usuario <= 3 and usuario >= 1:
            break

    if usuario == 1:
        defs.abrir_dados()

    elif usuario == 2:
        nome = str(input('Digite o nome: ')).strip().capitalize()
        while nome == '':
            print('ERRO! O campo nome não pode ficar vazio. Tente Novamente!')
            nome = str(input('Digite o nome: ')).strip()

        while True:
            try:
                idade = int(input('Digite a idade: '))
                if idade > 0:
                    break

            except ValueError:
                print('ERRO! Por favor, digitar um valor inteiro! ')

        defs.cadastrar_pessoa(nome, idade)

    elif usuario == 3:
        print('-'*40)
        print('    SAINDO DO SISTEMA... ATE LOGO!')
        print('-' * 40)
        break

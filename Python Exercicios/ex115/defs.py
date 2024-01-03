def abrir_dados():
    try:
        pessoas_idades = open('dados', 'r')

    except FileNotFoundError:
        pessoas_idades = open('dados', 'w')

    file = open('dados', 'r')
    lista = list()
    for c in file:
        lista.append(c)

    if len(lista) == 0:
        print('ERRO! Não existe pessoas cadastradas')

    elif len(lista) > 0:
        lista_principal = list()
        lista_temporaria = list()
        contador = 0
        for c in pessoas_idades:
            if contador % 2 == 0:
                lista_temporaria.append(c.replace('\n', ''))
            else:
                lista_temporaria.append(c.replace('\n', ''))
                lista_principal.append(lista_temporaria.copy())
                lista_temporaria.clear()
            contador += 1

        for c in range(0, len(lista_principal)):
            print(f'{lista_principal[c][0]:<15} \t {lista_principal[c][1]:<2} anos')

def cadastrar_pessoa(nome, idade):
    try:
        file = open('dados', 'r')
        lista = list()
        for c in file:
            lista.append(c)
        if len(lista) > 1:
            file = open('dados', 'a')
            file.write(f'\n{nome}\n{idade}')
        elif len(lista) == 0:
            file = open('dados', 'a')
            file.write(f'{nome}\n{idade}')
        file.close()

    except FileNotFoundError:
        file = open('dados', 'w')
        file.write(f'{nome}\n{idade}')

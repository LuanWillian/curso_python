lista = list()
for c in range(0,5):
    numero = int(input('Digite um numero: '))
    if c == 0 or numero > lista[-1]:
        print('Adicionado no final da lista...')
        lista.append(numero)
    else:
        posiçao = 0
        while posiçao < len(lista):
            if numero <= lista[posiçao]:
                lista.insert(posiçao,numero)
                print(f'Adicionado na posição {posiçao} da lista...')
                break
            posiçao += 1
print('')
print(f'Os valores digitados em ordem foram {lista}')

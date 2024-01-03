expressão = str(input('Digite a expressão: '))
lista = list()
for c in expressão:
    if c == '(':
        lista.append('(')
    elif c == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua exprssão estar valida!')
else:
    print('Sua expressão estar invalida!')

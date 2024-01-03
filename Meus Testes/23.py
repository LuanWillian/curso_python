opção = 0
contador = 0
maior = 0
menor = 0
soma = 0
media = 0
while not opção == 'N':
    contador = contador +1
    numero = int(input('Numero: '))
    opção = str(input('Continuar? [S/N]: ')).upper().strip()[0]
    soma = soma + numero

    while not opção == 'N' and not opção == 'S':
        print('Ops, Opção errada! Tente Novamente!')
        opção = str(input('Continuar? [S/N]: ')).upper().strip()[0]

    if contador == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

media = soma / contador
print('A media dos numeros são {}'.format(media))
print('O maior numero foi {} e menor foi {}'.format(maior,menor))
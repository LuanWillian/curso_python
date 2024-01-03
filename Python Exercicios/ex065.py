opção = ''
soma = 0
media = 0
contador = 1
maior = 0
menor = 0
while opção != 'N' or opção == 'S':
    valor = int(input('Digite um numero: '))
    opção = str(input('Continua? [S/N]: ')).upper()
    
    if contador == 1:
        maior = valor
        menor = valor
    else:
        if valor > menor:
            maior = valor
        if valor < menor:
            menor = valor

    if opção != 'N':
        contador = contador +1
        soma = soma + valor 
        media = soma / contador
print('A media dos numeros foi {}'.format(media))
print('O maior numero foi {} e o menor foi {}'.format(maior,menor))
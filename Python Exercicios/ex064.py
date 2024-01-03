opção = int(input('Digite um numero: '))
contador = 0
soma = 0
while not opção == 999:
    contador = contador +1
    soma = soma + opção
    opção = int(input('Digite um numero: '))
print('Voce digitou {} numeros, a soma dos numero foi {}'.format(contador,soma))

contador = 0
soma = 0
while True:
    numero = int(input('Digite um numero [999 para parar]: '))
    if numero == 999:
        break
    contador = contador +1
    soma = soma + numero
print(f'A soma dos {contador} numeros foi {soma}')
lista = [[], []]
for c in range(0,7):
    numero = int(input('Digite um numero: '))
    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)

lista[0].sort()
lista[1].sort()
print(f'Os numeros pares digitados foram {lista[0]}')
print(f'Os numeros impares digitados foram {lista[1]}')

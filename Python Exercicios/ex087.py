matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
somaColuna = 0
maior = 0
for c in range(0,3):
    for d in range(0,3):
        matriz[c][d] = int(input(f'Digite um numero para [{c},{d}]: '))

for c in range(0,3):
    for d in range(0,3):
        print(f'[{matriz[c][d]}]', end='')
        if d == 2:
            somaColuna += matriz[c][d]
        if matriz[c][d] % 2 == 0:
            soma += matriz[c][d]
    print()

for c in range(0,len(matriz[1])):
    if c == 0:
        maior = matriz[1][c]
    else:
        if maior < matriz[1][c]:
            maior = matriz[1][c]

print(f'A soma dos numeros pares e {soma}')
print(f'A soma dos numeros da terceira coluna e {somaColuna}')
print(f'O maior valor da segunda linha e {maior}')

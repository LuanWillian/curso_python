valores = list()
for numeros in range(0,3):
    valores.append(int(input(('Digite um numero: '))))

for posicao, c in enumerate(valores):
    print(f'Na posição {posicao} encontrei o valor {c}!')
print('Cheguei no final da lista.')

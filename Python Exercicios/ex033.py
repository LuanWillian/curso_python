n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

#Vai clasificar se uma variavel e menor do que outra variavel
if n1<n2 and n1<n3:
    menor = n1

if n2<n1 and n2<n3:
    menor = n2

if n3<n1 and n3<n2:
    menor =  n3

print('O menor numero e {}'.format(menor))

#Vai clasificar se uma variavel e maior do que outra variavel
if n1>n2 and n1>n3:
    maior = n1

if n2>n3 and n2>n1:
    maior = n2

if n3>n1 and n3>n2:
    menor = n3

print('O maior numero e {}'.format(maior))
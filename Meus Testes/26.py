nome = input('Digite seu nome: ')
a = nome.upper()
b = nome.lower()
c = nome.split()[0]

print('Seu nome em maiusculas: {} '.format(a))
print('Seu nome em minusculas: {} '.format(b))
print('Seu primeiro nome tem {} letras'.format(len(c)))
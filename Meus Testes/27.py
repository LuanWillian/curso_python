nome = str(input('Digite seu nome: '))

mais = nome.upper()
menos = nome.lower()
celecionado = len(nome.split()[0])
linpar = len(nome) - nome.count(' ')

print('Seu nome em maiusculas e: {}'.format(mais))
print('Seu nome em minusculas e: {}'.format(menos))
print('Seu primeiro nome tem {} letras'.format(celecionado))
print('Seu nome ao todo tem {}'.format(linpar))
nome = str(input('Digite uma frase: ')).upper().strip()
print('A letra "A" apareceu {} vezes'.format(nome.count('A')))
print('A letra "A" aparece na posiçao {}'.format(nome.find('A')+1))
print('A ultima letras "A" aparece na posiçao {}'.format(nome.rfind('A')+1))
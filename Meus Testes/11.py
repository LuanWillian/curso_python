frase = str(input('Digite uma frase: ')).strip()
separador = frase.split()
juntador = ''.join(separador)
resutado = juntador[::-1]

if resutado == juntador:
    print('Essa frase e polidromo!')
else:
    print('Essa frase não e polidromo!')

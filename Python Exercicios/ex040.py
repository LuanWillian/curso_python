nota1 = float(input('Digite sua nota: '))
nota2 = float(input('Digite sua nota: '))

if (nota1 + nota2) / 2 >= 7.0:
    print('Voce foi APROVADO!')

elif (nota1 + nota2) / 2 == 5.0 or 6.9:
    print('Voce ficou em RECUPERAÇÃO!')

elif (nota1 + nota2) / 2 < 5:
    print('Voce foi REPROVADO!')
